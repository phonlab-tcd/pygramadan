# coding=UTF-8
from .attributes import Mutation as M, VerbDependency, VerbMood, VerbPerson, VerbTense
from .attributes import VerbTense as VT
from .attributes import VerbDependency as VD
from .attributes import VerbMood as VM
from .attributes import VerbPerson as VPN
from .attributes import VPMood, VPPerson, VPPolarity, VPShape, VPTense
from .verb_tense_rule import VerbTenseRule
from .default_tense_rules import get_default_tense_rules
import xml.etree.ElementTree as ET
from typing import List
from .forms import Form

class Verb:
    def __init__(self,
                 source = None,
                 verbal_noun: List[Form] = None,
                 verbal_adj: List[Form] = None,
                 tenses = None,
                 moods = None
        ) -> None:
        self.tense_rules = get_default_tense_rules()
        self.verbal_noun: List[Form] = verbal_noun
        self.verbal_adj: List[Form] = verbal_adj

        if self.verbal_noun is None:
            self.verbal_noun = []
        if self.verbal_adj is None:
            self.verbal_adj = []
        if self.tenses is None:
            self.tenses = {}
            for t in VerbTense:
                tenses[t] = {}
                for d in VerbDependency:
                    tenses[t][d] = {}
                    for p in VerbPerson:
                        tenses[t][d][p] = []
        if self.moods is None:
            self.moods = {}
            for m in VerbMood:
                self.moods[m] = {}
                for p in VerbPerson:
                    self.moods[m][p] = []

    def get_tense_rules(self, tense: VPTense, person: VPPerson, shape: VPShape, polarity: VPPolarity):
        out = []
        def matches(t, per, s, pol):
            tm = tense == VPTense.Any or tense == t
            pm = person == VPPerson.Any or person == per
            sm = shape == VPShape.Any or shape == s
            polm = polarity == VPPolarity.Any or polarity == pol
            return tm and pm and sm and polm
        for t in VPTense:
            if t == VPTense.Any:
                continue
            for per in VPPerson:
                if per == VPPerson.Any:
                    continue
                for s in VPShape:
                    if s == VPShape.Any:
                        continue
                    for pol in VPPolarity:
                        if pol == VPPolarity.Any:
                            continue
                        if matches(t, per, s, pol):
                            for rule in self.tense_rules[t][per][s][pol]:
                                out.append(rule)
        return out

    def add_tense(self,
                  t: VerbTense = None,
                  d: VerbDependency = None,
                  p: VerbPerson = None,
                  form: str = ""):
        if t is None:
            raise Exception('Missing parameter `t` (tense)')
        if p is None:
            raise Exception('Missing parameter `p` (person)')
        if d is None:
            self.tenses[t][VerbDependency.Indep][p].append(Form(form))
            self.tenses[t][VerbDependency.Dep][p].append(Form(form))
        else:
            self.tenses[t][d][p].append(Form(form))

    def add_mood(self,
                 m: VerbMood = None,
                 p: VerbPerson = None,
                 form: str = ""):
        if m is None:
            raise Exception('Missing parameter `m` (mood)')
        if p is None:
            raise Exception('Missing parameter `p` (person)')
        if str == "":
            raise Exception('Missing parameter `form`')

    def from_xml(self, source) -> None:
        tree = ET.parse(source)
        root = tree.getroot()

        self.disambig = root.attrib['disambig']

        for form in root.findall('./verbalNoun'):
            value = form.attrib.get('default')
            self.verbal_noun.append(Form(value))
        for form in root.findall('./verbalAdjective'):
            value = form.attrib.get('default')
            self.verbal_adj.append(Form(value))
        for form in root.findall('./tenseForm'):
            value = form.attrib.get('default')
            raw_tense = form.attrib.get('tense')
            if raw_tense in VerbTense.__members__:
                tense = VerbTense[raw_tense]
            else:
                raise Exception(f'Unknown tense form: {raw_tense}')
            raw_dep = form.attrib.get('dependency')
            if raw_dep in VerbDependency.__members__:
                dependency = VerbDependency[raw_dep]
            else:
                raise Exception(f'Unknown dependency form: {raw_dep}')
            raw_pers = form.attrib.get('person')
            if raw_pers in VerbPerson.__members__:
                person = VerbPerson[raw_pers]
            else:
                raise Exception(f'Unknown person form: {raw_pers}')
            self.add_tense(tense, dependency, person, value)
        for form in root.findall('./moodForm'):
            value = form.attrib.get('default')
            raw_mood = form.attrib.get('mood')
            if raw_mood in VerbMood.__members__:
                mood = VerbMood[raw_mood]
            else:
                raise Exception(f'Unknown mood form: {raw_mood}')
            raw_pers = form.attrib.get('person')
            if raw_pers in VerbPerson.__members__:
                person = VerbPerson[raw_pers]
            else:
                raise Exception(f'Unknown person form: {raw_pers}')
            self.add_mood(mood, person, value)

    def to_xml(self):
        props = {}
        props['default'] = self.get_lemma()
        props['disambig'] = self.disambig
        root = ET.Element('verb', props)
        for form in self.verbal_noun:
            _ = ET.SubElement(root, 'verbalNoun', {'default': form.value})
        for form in self.verbal_adj:
            _ = ET.SubElement(root, 'verbalAdjective', {'default': form.value})
        for tense in self.tenses:
            for dependency in self.tenses[tense]:
                for person in self.tenses[tense][dependency]:
                    for form in self.tenses[tense][dependency][person]:
                        tprops = {}
                        tprops['default'] = form.value
                        tprops['tense'] = tense.name
                        tprops['dependency'] = dependency.name
                        tprops['person'] = person.name
                        _ = ET.SubElement(root, 'tenseForm', tprops)
        for mood in self.moods:
            for person in self.moods[mood]:
                for form in self.moods[mood][person]:
                    tprops = {}
                    tprops['default'] = form.value
                    tprops['mood'] = mood.name
                    tprops['person'] = person.name
                    _ = ET.SubElement(root, 'moodForm', tprops)

        return ET.tostring(root, encoding='UTF-8')

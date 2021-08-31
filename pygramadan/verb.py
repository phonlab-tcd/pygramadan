# coding=UTF-8
from .attributes import Mutation as M, VerbDependency, VerbMood, VerbPerson, VerbTense
from .attributes import VPPerson, VPPolarity, VPShape, VPTense
from .default_tense_rules import get_default_tense_rules
import xml.etree.ElementTree as ET
from typing import List
from .forms import Form


class Verb:
    def __init__(self,
                 disambig: str = "",
                 source = None,
                 verbal_noun: List[Form] = None,
                 verbal_adj: List[Form] = None,
                 tenses = None,
                 moods = None) -> None:
        self.disambig = disambig
        self.tense_rules = get_default_tense_rules()
        self.verbal_noun: List[Form] = verbal_noun
        self.verbal_adj: List[Form] = verbal_adj
        self.tenses = tenses
        self.moods = moods

        if self.verbal_noun is None:
            self.verbal_noun = []
        if self.verbal_adj is None:
            self.verbal_adj = []
        if self.tenses is None:
            self.tenses = init_tenses()
        if self.moods is None:
            self.moods = init_moods()

        if source is not None:
            self._clear()
            self.from_xml(source)

    def _clear(self):
        self.disambig = ""
        self.verbal_adj = []
        self.verbal_noun = []
        self.tenses = init_tenses()
        self.moods = init_moods()
        self.tense_rules = get_default_tense_rules()

    def get_tense_rules(self, tense: VPTense, person: VPPerson, shape: VPShape, polarity: VPPolarity):  # noqa: C901
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

    def get_lemma(self) -> str:
        if len(self.moods[VerbMood.Imper][VerbPerson.Sg2]) > 0:
            return self.moods[VerbMood.Imper][VerbPerson.Sg2][0].value
        elif len(self.tenses[VerbTense.Past][VerbDependency.Indep][VerbPerson.Base]) > 0:
            return self.tenses[VerbTense.Past][VerbDependency.Indep][VerbPerson.Base][0].value
        else:
            return ""

    def get_identifier(self) -> str:
        """
        Get an identifier for this verb
        Note: called getNickname() in Gramadán
        """
        disambig = ""
        if self.disambig != "":
            disambig = "_" + self.disambig
        outlem = self.get_lemma().replace(" ", "_")
        return f'{outlem}_verb{disambig}'

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
        if form == "":
            raise Exception('Missing parameter `form`')
        self.moods[m][p].append(Form(form))

    def from_xml(self, source) -> None:
        """
        Initialise from XML in BuNaMo format:

        >>> from pygramadan.verb import Verb, get_example
        >>> import io
        >>> xml = get_example()
        >>> sio = io.StringIO(xml)
        >>> aimsigh = Verb(source=sio)
        """
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

        self._modify_rules(self.get_lemma())

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

    def get_all_forms(self):
        """
        Returns a list of tuples, `(form-description, form)`:

        >>> aimsigh.get_all_forms()
        [('fut_dep_pl1', 'aimseoimid'), ('pastcont_indep_sg2', 'aimsíteá') ... ]
        """
        forms = set()
        for verbal_noun in self.verbal_noun:
            tpl = ('verbal_noun', verbal_noun.value)
            forms.add(tpl)
        for verbal_adj in self.verbal_adj:
            tpl = ('verbal_adj', verbal_adj.value)
            forms.add(tpl)
        for tense in self.tenses:
            for dependency in self.tenses[tense]:
                for person in self.tenses[tense][dependency]:
                    for form in self.tenses[tense][dependency][person]:
                        desc = f'{tense.name}_{dependency.name}_{person.name}'.lower()
                        tpl = (desc, form.value)
                        forms.add(tpl)
        for mood in self.moods:
            for person in self.moods[mood]:
                for form in self.moods[mood][person]:
                        desc = f'{mood.name}_{person.name}'.lower()
                        tpl = (desc, form.value)
                        forms.add(tpl)
        return list(forms)

    def _modify_rules(self, lemma: str) -> None:
        if lemma == 'bí':
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Declar, VPPolarity.Pos):
                rule.mutation = M.Len1
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Declar, VPPolarity.Neg):
                rule.mutation = M.NoMut
                rule.particle = 'ní'
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Interrog, VPPolarity.Pos):
                rule.mutation = M.NoMut
                rule.particle = 'an'
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Interrog, VPPolarity.Neg):
                rule.mutation = M.NoMut
                rule.particle = 'nach'
        if lemma == 'abair':
            for rule in self.get_tense_rules(VPTense.Any, VPPerson.Any, VPShape.Declar, VPPolarity.Pos):
                rule.mutation = M.NoMut
            for rule in self.get_tense_rules(VPTense.Any, VPPerson.Any, VPShape.Declar, VPPolarity.Neg):
                rule.mutation = M.NoMut
                rule.particle = 'ní'
            for rule in self.get_tense_rules(VPTense.Any, VPPerson.Any, VPShape.Interrog, VPPolarity.Pos):
                rule.mutation = M.Ecl1x
                rule.particle = 'an'
            for rule in self.get_tense_rules(VPTense.Any, VPPerson.Any, VPShape.Interrog, VPPolarity.Neg):
                rule.mutation = M.Ecl1
                rule.particle = 'nach'
        if lemma == 'déan':
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Declar, VPPolarity.Neg):
                rule.mutation = M.Len1
                rule.particle = 'ní'
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Interrog, VPPolarity.Pos):
                rule.mutation = M.Ecl1x
                rule.particle = 'an'
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Interrog, VPPolarity.Neg):
                rule.mutation = M.Ecl1
                rule.particle = 'nach'
        if lemma == 'faigh':
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Declar, VPPolarity.Pos):
                rule.mutation = M.NoMut
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Declar, VPPolarity.Neg):
                rule.mutation = M.Ecl1
                rule.particle = 'ní'
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Interrog, VPPolarity.Pos):
                rule.mutation = M.Ecl1x
                rule.particle = 'an'
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Interrog, VPPolarity.Neg):
                rule.mutation = M.Ecl1
                rule.particle = 'nach'
            for rule in self.get_tense_rules(VPTense.Fut, VPPerson.Any, VPShape.Declar, VPPolarity.Pos):
                rule.mutation = M.Len1
            for rule in self.get_tense_rules(VPTense.Fut, VPPerson.Any, VPShape.Declar, VPPolarity.Neg):
                rule.mutation = M.Ecl1
                rule.particle = 'ní'
            for rule in self.get_tense_rules(VPTense.Fut, VPPerson.Any, VPShape.Interrog, VPPolarity.Pos):
                rule.mutation = M.Ecl1x
                rule.particle = 'an'
            for rule in self.get_tense_rules(VPTense.Fut, VPPerson.Any, VPShape.Interrog, VPPolarity.Neg):
                rule.mutation = M.Ecl1
                rule.particle = 'nach'
            for rule in self.get_tense_rules(VPTense.Cond, VPPerson.Any, VPShape.Declar, VPPolarity.Neg):
                rule.mutation = M.Ecl1
                rule.particle = 'ní'
        if lemma in ['feic', 'téigh']:
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Declar, VPPolarity.Pos):
                rule.mutation = M.Len1
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Declar, VPPolarity.Neg):
                rule.mutation = M.Len1
                rule.particle = 'ní'
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Interrog, VPPolarity.Pos):
                rule.mutation = M.Ecl1x
                rule.particle = 'an'
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Any, VPShape.Interrog, VPPolarity.Neg):
                rule.mutation = M.Ecl1
                rule.particle = 'nach'
        if lemma in ['tar', 'clois', 'cluin']:
            for rule in self.get_tense_rules(VPTense.Past, VPPerson.Auto, VPShape.Any, VPPolarity.Any):
                rule.mutation = M.Len1


def init_tenses():
    """initialises the tenses dict."""
    tenses = {}
    for t in VerbTense:
        tenses[t] = {}
        for d in VerbDependency:
            tenses[t][d] = {}
            for p in VerbPerson:
                tenses[t][d][p] = []
    return tenses


def init_moods():
    """initialises the moods dict."""
    moods = {}
    for m in VerbMood:
        moods[m] = {}
        for p in VerbPerson:
            moods[m][p] = []
    return moods


def get_example():
    return """\
<verb default="aimsigh" disambig="">
  <verbalNoun default="aimsiú" />
  <verbalAdjective default="aimsithe" />
  <tenseForm default="aimsigh" tense="Past" dependency="Indep" person="Base" />
  <tenseForm default="aimsíomar" tense="Past" dependency="Indep" person="Pl1" />
  <tenseForm default="aimsíodar" tense="Past" dependency="Indep" person="Pl3" />
  <tenseForm default="aimsíodh" tense="Past" dependency="Indep" person="Auto" />
  <tenseForm default="aimsigh" tense="Past" dependency="Dep" person="Base" />
  <tenseForm default="aimsíomar" tense="Past" dependency="Dep" person="Pl1" />
  <tenseForm default="aimsíodar" tense="Past" dependency="Dep" person="Pl3" />
  <tenseForm default="aimsíodh" tense="Past" dependency="Dep" person="Auto" />
  <tenseForm default="aimsíodh" tense="PastCont" dependency="Indep" person="Base" />
  <tenseForm default="aimsínn" tense="PastCont" dependency="Indep" person="Sg1" />
  <tenseForm default="aimsíteá" tense="PastCont" dependency="Indep" person="Sg2" />
  <tenseForm default="aimsímis" tense="PastCont" dependency="Indep" person="Pl1" />
  <tenseForm default="aimsídís" tense="PastCont" dependency="Indep" person="Pl3" />
  <tenseForm default="aimsítí" tense="PastCont" dependency="Indep" person="Auto" />
  <tenseForm default="aimsíodh" tense="PastCont" dependency="Dep" person="Base" />
  <tenseForm default="aimsínn" tense="PastCont" dependency="Dep" person="Sg1" />
  <tenseForm default="aimsíteá" tense="PastCont" dependency="Dep" person="Sg2" />
  <tenseForm default="aimsímis" tense="PastCont" dependency="Dep" person="Pl1" />
  <tenseForm default="aimsídís" tense="PastCont" dependency="Dep" person="Pl3" />
  <tenseForm default="aimsítí" tense="PastCont" dependency="Dep" person="Auto" />
  <tenseForm default="aimsíonn" tense="PresCont" dependency="Indep" person="Base" />
  <tenseForm default="aimsím" tense="PresCont" dependency="Indep" person="Sg1" />
  <tenseForm default="aimsímid" tense="PresCont" dependency="Indep" person="Pl1" />
  <tenseForm default="aimsítear" tense="PresCont" dependency="Indep" person="Auto" />
  <tenseForm default="aimsíonn" tense="PresCont" dependency="Dep" person="Base" />
  <tenseForm default="aimsím" tense="PresCont" dependency="Dep" person="Sg1" />
  <tenseForm default="aimsímid" tense="PresCont" dependency="Dep" person="Pl1" />
  <tenseForm default="aimsítear" tense="PresCont" dependency="Dep" person="Auto" />
  <tenseForm default="aimseoidh" tense="Fut" dependency="Indep" person="Base" />
  <tenseForm default="aimseoimid" tense="Fut" dependency="Indep" person="Pl1" />
  <tenseForm default="aimseofar" tense="Fut" dependency="Indep" person="Auto" />
  <tenseForm default="aimseoidh" tense="Fut" dependency="Dep" person="Base" />
  <tenseForm default="aimseoimid" tense="Fut" dependency="Dep" person="Pl1" />
  <tenseForm default="aimseofar" tense="Fut" dependency="Dep" person="Auto" />
  <tenseForm default="aimseodh" tense="Cond" dependency="Indep" person="Base" />
  <tenseForm default="aimseoinn" tense="Cond" dependency="Indep" person="Sg1" />
  <tenseForm default="aimseofá" tense="Cond" dependency="Indep" person="Sg2" />
  <tenseForm default="aimseoimis" tense="Cond" dependency="Indep" person="Pl1" />
  <tenseForm default="aimseoidís" tense="Cond" dependency="Indep" person="Pl3" />
  <tenseForm default="aimseofaí" tense="Cond" dependency="Indep" person="Auto" />
  <tenseForm default="aimseodh" tense="Cond" dependency="Dep" person="Base" />
  <tenseForm default="aimseoinn" tense="Cond" dependency="Dep" person="Sg1" />
  <tenseForm default="aimseofá" tense="Cond" dependency="Dep" person="Sg2" />
  <tenseForm default="aimseoimis" tense="Cond" dependency="Dep" person="Pl1" />
  <tenseForm default="aimseoidís" tense="Cond" dependency="Dep" person="Pl3" />
  <tenseForm default="aimseofaí" tense="Cond" dependency="Dep" person="Auto" />
  <moodForm default="aimsíodh" mood="Imper" person="Base" />
  <moodForm default="aimsím" mood="Imper" person="Sg1" />
  <moodForm default="aimsigh" mood="Imper" person="Sg2" />
  <moodForm default="aimsímis" mood="Imper" person="Pl1" />
  <moodForm default="aimsígí" mood="Imper" person="Pl2" />
  <moodForm default="aimsídís" mood="Imper" person="Pl3" />
  <moodForm default="aimsítear" mood="Imper" person="Auto" />
  <moodForm default="aimsí" mood="Subj" person="Base" />
  <moodForm default="aimsímid" mood="Subj" person="Pl1" />
  <moodForm default="aimsítear" mood="Subj" person="Auto" />
</verb>
"""

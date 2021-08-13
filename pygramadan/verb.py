# coding=UTF-8
from .attributes import Mutation as M
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
                 verbal_adj: List[Form] = None
        ) -> None:
        self.tense_rules = get_default_tense_rules()
        self.verbal_noun: List[Form] = verbal_noun
        self.verbal_adj: List[Form] = verbal_adj

        if self.verbal_noun == None:
            self.verbal_noun = []
        if self.verbal_adj == None:
            self.verbal_adj = []

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

    def from_xml(self, source):
        pass

    def to_xml(self):
        props = {}
        props['default'] = self.get_lemma()
        props['disambig'] = self.disambig
        root = ET.Element('noun', props)
        for form in self.verbal_noun:
            _ = ET.SubElement(root, 'verbalNoun', {'default': form.value})
        for form in self.verbal_adj:
            _ = ET.SubElement(root, 'verbalAdjective', {'default': form.value})

# coding=UTF-8
from .attributes import Mutation as M
from .attributes import VerbTense as VT
from .attributes import VerbDependency as VD
from .attributes import VerbMood as VM
from .attributes import VerbPerson as VPN
from .attributes import VPMood, VPPerson, VPPolarity, VPShape, VPTense
from .default_tense_rules import get_default_tense_rules


class VerbTenseRule:
    def __init__(self,
                 particle: str = "",
                 mutation: M = M.NoMut,
                 tense: VT = VT.Pres,
                 dependency: VD = VD.Indep,
                 person: VPN = VPN.Base,
                 pronoun: str = "") -> None:
        self.particle = particle
        self.mutation = mutation
        self.tense = tense
        self.dependency = dependency
        self.person = person
        self.pronoun = pronoun


class Verb:
    def __init__(self) -> None:
        self.tense_rules = get_default_tense_rules()

    def get_tense_rules(self, tense: VPTense, person: VPPerson, shape: VPShape, polarity: VPPolarity):
        out = []
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
                        if ((tense == VPTense.Any or tense == t) and \
                            (person == VPPerson.Any or person == p) and \
                            (shape == VPShape.Any or shape == s) and \
                            (polarity == VPPolarity.Any or polarity == pol)):
                            for rule in self.tense_rules[t][per][s][pol]:
                                out.append(rule)
        return out
# coding=UTF-8
from .attributes import Mutation as M
from .attributes import VerbTense as VT
from .attributes import VerbDependency as VD
from .attributes import VerbMood as VM
from .attributes import VerbPerson as VPN
from .attributes import VPMood, VPPerson, VPPolarity, VPShape, VPTense

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

        # ewwwwww
        self.tense_rules = {}
        for tense in VPTense:
            if tense == VPTense.Any:
                continue
            self.tense_rules[tense] = {}
            for person in VPPerson:
                if person == VPPerson.Any:
                    continue
                self.tense_rules[tense][person] = {}
                for shape in VPShape:
                    if shape == VPShape.Any:
                        continue
                    self.tense_rules[tense][person][shape] = {}
                    for polarity in VPPolarity:
                        if polarity == VPPolarity.Any:
                            continue
                        self.tense_rules[tense][person][shape][polarity] = []

            
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

        dec: VPShape = VPShape.Declar
        rog: VPShape = VPShape.Interrog
        pos: VPPolarity = VPPolarity.Pos
        neg: VPPolarity = VPPolarity.Neg

        # cheap, d'oscail
        t = VPTense.Past
        p = VPPerson.NoSubject
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Past, VD.Indep, VPN.Base, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("níor", M.Len1, VT.Past, VD.Dep, VPN.Base, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("ar", M.Len1, VT.Past, VD.Dep, VPN.Base, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nár", M.Len1, VT.Past, VD.Dep, VPN.Base, ""))

        # cheap mé, d'oscail mé
        p = VPPerson.Sg1
        pron = "mé"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Past, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("níor", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("ar", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nár", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))

        # cheap tú, d'oscail tú
        p = VPPerson.Sg2
        pron = "tú"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Past, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("níor", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("ar", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nár", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))

        # cheap sé, d'oscail sé
        p = VPPerson.Sg3Masc
        pron = "sé"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Past, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("níor", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("ar", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nár", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))

        # cheap sí, d'oscail sí
        p = VPPerson.Sg3Fem
        pron = "sí"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Past, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("níor", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("ar", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nár", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))

        # cheapamar, d'osclaíomar
        p = VPPerson.Pl1
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Past, VD.Indep, VPN.Pl1, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("níor", M.Len1, VT.Past, VD.Dep, VPN.Pl1, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("ar", M.Len1, VT.Past, VD.Dep, VPN.Pl1, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nár", M.Len1, VT.Past, VD.Dep, VPN.Pl1, ""))

        # cheap muid, d'oscail muid
        p = VPPerson.Pl1
        pron = "muid"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Past, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("níor", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("ar", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nár", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))

        # cheap sibh, d'oscail sibh
        p = VPPerson.Pl2
        pron = "sibh"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Past, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("níor", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("ar", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nár", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))

        # cheap siad, d'oscail siad
        p = VPPerson.Pl3
        pron = "siad"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Past, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("níor", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("ar", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nár", M.Len1, VT.Past, VD.Dep, VPN.Base, pron))

        # cheapadar, d'osclaíodar
        p = VPPerson.Pl3
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Past, VD.Indep, VPN.Pl3, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("níor", M.Len1, VT.Past, VD.Dep, VPN.Pl3, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("ar", M.Len1, VT.Past, VD.Dep, VPN.Pl3, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nár", M.Len1, VT.Past, VD.Dep, VPN.Pl3, ""))

        # 
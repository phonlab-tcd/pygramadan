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

        # ceapadh, osclaíodh
        p = VPPerson.Auto
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Past, VD.Indep, VPN.Auto, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("níor", M.NoMut, VT.Past, VD.Dep, VPN.Auto, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("ar", M.NoMut, VT.Past, VD.Dep, VPN.Auto, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nár", M.NoMut, VT.Past, VD.Dep, VPN.Auto, ""))

        # Only 'bí' has forms in this tense.
        t = VPTense.Pres
        # tá
        p = VPPerson.NoSubject
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Pres, VD.Indep, VPN.Base, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Pres, VD.Dep, VPN.Base, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Pres, VD.Dep, VPN.Base, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Pres, VD.Dep, VPN.Base, ""))

        # táim
        p = VPPerson.Sg1
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Pres, VD.Indep, VPN.Sg1, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Pres, VD.Dep, VPN.Sg1, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Pres, VD.Dep, VPN.Sg1, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Pres, VD.Dep, VPN.Sg1, ""))

        # tá mé
        p = VPPerson.Sg1
        pron = "mé"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Pres, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Pres, VD.Dep, VPN.Base, pron))

        # tá tú
        p = VPPerson.Sg2
        pron = "tú"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Pres, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Pres, VD.Dep, VPN.Base, pron))

        # tá sé
        p = VPPerson.Sg3Masc
        pron = "sé"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Pres, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Pres, VD.Dep, VPN.Base, pron))

        # tá sí
        p = VPPerson.Sg3Fem
        pron = "sí"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Pres, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Pres, VD.Dep, VPN.Base, pron))

        # táimid
        p = VPPerson.Pl1
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Pres, VD.Indep, VPN.Pl1, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Pres, VD.Dep, VPN.Pl1, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Pres, VD.Dep, VPN.Pl1, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Pres, VD.Dep, VPN.Pl1, ""))

        # tá muid
        p = VPPerson.Pl1
        pron = "muid"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Pres, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Pres, VD.Dep, VPN.Base, pron))

        # tá sibh
        p = VPPerson.Pl2
        pron = "sibh"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Pres, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Pres, VD.Dep, VPN.Base, pron))

        # tá siad
        p = VPPerson.Pl3
        pron = "siad"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Pres, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Pres, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Pres, VD.Dep, VPN.Base, pron))

        # táthar
        p = VPPerson.Auto
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Pres, VD.Indep, VPN.Auto, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Pres, VD.Dep, VPN.Auto, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Pres, VD.Dep, VPN.Auto, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Pres, VD.Dep, VPN.Auto, ""))

        # ceapann, osclaíonn
        t = VPTense.PresCont
        p = VPPerson.NoSubject
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.PresCont, VD.Indep, VPN.Base, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PresCont, VD.Dep, VPN.Base, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PresCont, VD.Dep, VPN.Base, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PresCont, VD.Dep, VPN.Base, ""))

        # ceapaim, osclaím
        p = VPPerson.Sg1;
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.PresCont, VD.Indep, VPN.Sg1, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PresCont, VD.Dep, VPN.Sg1, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PresCont, VD.Dep, VPN.Sg1, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PresCont, VD.Dep, VPN.Sg1, ""))

        # ceapann tú, osclaíonn tú
        p = VPPerson.Sg2
        pron = "tú"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.PresCont, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PresCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PresCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PresCont, VD.Dep, VPN.Base, pron))

        # ceapann sé, osclaíonn sé
        p = VPPerson.Sg3Masc
        pron = "sé"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.PresCont, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PresCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PresCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PresCont, VD.Dep, VPN.Base, pron))

        # ceapann sí, osclaíonn sí
        p = VPPerson.Sg3Fem
        pron = "sí"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.PresCont, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PresCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PresCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PresCont, VD.Dep, VPN.Base, pron))

        # ceapaimid, osclaímid
        p = VPPerson.Pl1
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.PresCont, VD.Indep, VPN.Pl1, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PresCont, VD.Dep, VPN.Pl1, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PresCont, VD.Dep, VPN.Pl1, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PresCont, VD.Dep, VPN.Pl1, ""))

        # ceapann muid, osclaíonn muid
        p = VPPerson.Pl1
        pron = "muid"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.PresCont, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PresCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PresCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PresCont, VD.Dep, VPN.Base, pron))

        # ceapann sibh, osclaíonn sibh
        p = VPPerson.Pl2
        pron = "sibh"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.PresCont, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PresCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PresCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PresCont, VD.Dep, VPN.Base, pron))

        # ceapann siad, osclaíonn siad
        p = VPPerson.Pl3
        pron = "siad"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.PresCont, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PresCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PresCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PresCont, VD.Dep, VPN.Base, pron))

        # ceaptar, osclaítear
        p = VPPerson.Auto
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.PresCont, VD.Indep, VPN.Auto, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PresCont, VD.Dep, VPN.Auto, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PresCont, VD.Dep, VPN.Auto, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PresCont, VD.Dep, VPN.Auto, ""))

        # ceapfaidh, osclóidh
        t = VPTense.Fut
        p = VPPerson.NoSubject
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Fut, VD.Indep, VPN.Base, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Fut, VD.Dep, VPN.Base, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Fut, VD.Dep, VPN.Base, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Fut, VD.Dep, VPN.Base, ""))

        # ceapfaidh mé, osclóidh mé
        p = VPPerson.Sg1
        pron = "mé"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Fut, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Fut, VD.Dep, VPN.Base, pron))

        # ceapfaidh tú, osclóidh tú
        p = VPPerson.Sg2
        pron = "tú"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Fut, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Fut, VD.Dep, VPN.Base, pron))

        # ceapfaidh sé, osclóidh sé
        p = VPPerson.Sg3Masc
        pron = "sé"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Fut, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Fut, VD.Dep, VPN.Base, pron))

        # ceapfaidh sí, osclóidh sí
        p = VPPerson.Sg3Fem
        pron = "sí"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Fut, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Fut, VD.Dep, VPN.Base, pron))

        # ceapfaimid, osclóimid	
        p = VPPerson.Pl1
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Fut, VD.Indep, VPN.Pl1, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Fut, VD.Dep, VPN.Pl1, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Fut, VD.Dep, VPN.Pl1, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Fut, VD.Dep, VPN.Pl1, ""))

        # ceapfaidh muid, osclóidh muid
        p = VPPerson.Pl1
        pron = "muid"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Fut, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Fut, VD.Dep, VPN.Base, pron))

        # ceapfaidh sibh, osclóidh sibh
        p = VPPerson.Pl2
        pron = "sibh"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Fut, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Fut, VD.Dep, VPN.Base, pron))

        # ceapfaidh siad, osclóidh siad
        p = VPPerson.Pl3
        pron = "siad"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Fut, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Fut, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Fut, VD.Dep, VPN.Base, pron))

        # ceapfar, osclófar
        p = VPPerson.Auto
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.NoMut, VT.Fut, VD.Indep, VPN.Auto, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Fut, VD.Dep, VPN.Auto, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Fut, VD.Dep, VPN.Auto, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Fut, VD.Dep, VPN.Auto, ""))

        # cheapfadh, d'osclódh
        t = VPTense.Cond
        p = VPPerson.NoSubject
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Cond, VD.Indep, VPN.Base, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Cond, VD.Dep, VPN.Base, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Cond, VD.Dep, VPN.Base, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Cond, VD.Dep, VPN.Base, ""))

        # cheapfainn, d'osclóinn
        p = VPPerson.Sg1
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Cond, VD.Indep, VPN.Sg1, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Cond, VD.Dep, VPN.Sg1, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Cond, VD.Dep, VPN.Sg1, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Cond, VD.Dep, VPN.Sg1, ""))

        # cheapfá, d'osclófá
        p = VPPerson.Sg2
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Cond, VD.Indep, VPN.Sg2, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Cond, VD.Dep, VPN.Sg2, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Cond, VD.Dep, VPN.Sg2, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Cond, VD.Dep, VPN.Sg2, ""))

        # cheapfadh sé, d'osclódh sé
        p = VPPerson.Sg3Masc
        pron = "sé"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Cond, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Cond, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Cond, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Cond, VD.Dep, VPN.Base, pron))

        # cheapfadh sí, d'osclódh sí
        p = VPPerson.Sg3Fem
        pron = "sí"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Cond, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Cond, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Cond, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Cond, VD.Dep, VPN.Base, pron))

        # cheapfaimis, d'osclóimis
        p = VPPerson.Pl1
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Cond, VD.Indep, VPN.Pl1, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Cond, VD.Dep, VPN.Pl1, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Cond, VD.Dep, VPN.Pl1, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Cond, VD.Dep, VPN.Pl1, ""))

        p = VPPerson.Pl1 pron = "muid"; //cheapfadh muid, d'osclódh muid
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Cond, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Cond, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Cond, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Cond, VD.Dep, VPN.Base, pron))

        # cheapfadh sibh, d'osclódh sibh
        p = VPPerson.Pl2
        pron = "sibh"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Cond, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Cond, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Cond, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Cond, VD.Dep, VPN.Base, pron))

        # cheapfaidís, d'osclóidís
        p = VPPerson.Pl3
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Cond, VD.Indep, VPN.Pl3, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Cond, VD.Dep, VPN.Pl3, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Cond, VD.Dep, VPN.Pl3, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Cond, VD.Dep, VPN.Pl3, ""))

        # cheapfadh siad, d'osclódh siad
        p = VPPerson.Pl3
        pron = "siad"
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Cond, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Cond, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Cond, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Cond, VD.Dep, VPN.Base, pron))

        # cheapfaí, d'osclófaí
        p = VPPerson.Auto
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.Cond, VD.Indep, VPN.Auto, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.Cond, VD.Dep, VPN.Auto, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.Cond, VD.Dep, VPN.Auto, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.Cond, VD.Dep, VPN.Auto, ""))

        # cheapadh, d'osclaíodh
        t = VPTense.PastCont
        p = VPPerson.NoSubject
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.PastCont, VD.Indep, VPN.Base, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PastCont, VD.Dep, VPN.Base, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PastCont, VD.Dep, VPN.Base, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PastCont, VD.Dep, VPN.Base, ""))

        p = VPPerson.Sg1
        # cheapainn, d'osclaínn
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.PastCont, VD.Indep, VPN.Sg1, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PastCont, VD.Dep, VPN.Sg1, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PastCont, VD.Dep, VPN.Sg1, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PastCont, VD.Dep, VPN.Sg1, ""))

        p = VPPerson.Sg2
        # cheaptá, d'osclaíteá
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.PastCont, VD.Indep, VPN.Sg2, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PastCont, VD.Dep, VPN.Sg2, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PastCont, VD.Dep, VPN.Sg2, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PastCont, VD.Dep, VPN.Sg2, ""))

        p = VPPerson.Sg3Masc
        pron = "sé"
        # cheapadh sé, d'osclaíodh sé
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.PastCont, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PastCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PastCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PastCont, VD.Dep, VPN.Base, pron))

        p = VPPerson.Sg3Fem
        pron = "sí"
        # cheapadh sí, d'osclaíodh sí
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.PastCont, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PastCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PastCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PastCont, VD.Dep, VPN.Base, pron))

        p = VPPerson.Pl1
        # cheapaimis, d'osclaímis
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.PastCont, VD.Indep, VPN.Pl1, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PastCont, VD.Dep, VPN.Pl1, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PastCont, VD.Dep, VPN.Pl1, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PastCont, VD.Dep, VPN.Pl1, ""))

        p = VPPerson.Pl1
        pron = "muid"
        # cheapadh muid, d'osclaíodh muid
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.PastCont, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PastCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PastCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PastCont, VD.Dep, VPN.Base, pron))

        p = VPPerson.Pl2
        pron = "sibh"
        # cheapadh sibh, d'osclaíodh sibh
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.PastCont, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PastCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PastCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PastCont, VD.Dep, VPN.Base, pron))

        p = VPPerson.Pl3
        # cheapaidís, d'osclaídís
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.PastCont, VD.Indep, VPN.Pl3, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PastCont, VD.Dep, VPN.Pl3, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PastCont, VD.Dep, VPN.Pl3, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PastCont, VD.Dep, VPN.Pl3, ""))

        p = VPPerson.Pl3
        pron = "siad"
        # cheapadh siad, d'osclaíodh siad
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.PastCont, VD.Indep, VPN.Base, pron))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PastCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PastCont, VD.Dep, VPN.Base, pron))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PastCont, VD.Dep, VPN.Base, pron))

        p = VPPerson.Auto
        # cheaptaí, d'osclaítí
        self.tense_rules[t][p][dec][pos].append(VerbTenseRule("", M.Len1D, VT.PastCont, VD.Indep, VPN.Auto, ""))
        self.tense_rules[t][p][dec][neg].append(VerbTenseRule("ní", M.Len1, VT.PastCont, VD.Dep, VPN.Auto, ""))
        self.tense_rules[t][p][rog][pos].append(VerbTenseRule("an", M.Ecl1x, VT.PastCont, VD.Dep, VPN.Auto, ""))
        self.tense_rules[t][p][rog][neg].append(VerbTenseRule("nach", M.Ecl1, VT.PastCont, VD.Dep, VPN.Auto, ""))

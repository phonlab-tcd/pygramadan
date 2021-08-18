# coding=UTF-8
from pygramadan.verb_tense_rule import VerbTenseRule
from .attributes import Mutation, PERSON_MAP, VPMood, VPPerson, VPPolarity, VPShape, VPTense, VerbMood, VerbPerson
from .verb import Verb
from .opers import mutate
from .forms import Form


class VP:
    def __init__(self,
                 v: Verb = None) -> None:
        self.tenses = init_tenses()
        self.moods = init_moods()

        if v is not None:
            self._init_verb(v)

    def _init_verb(self, v: Verb) -> None:
        def check_nil(tm, sm, lm, valuem):
            a: bool = v.get_lemma == 'bí'
            b: bool = tm == VPTense.Pres
            c: bool = sm == VPShape.Declar
            d: bool = lm == VPPolarity.Neg
            e: bool = valuem.startswith('fhuil')
            return a and b and c and d and e
        t: VPTense = None
        p: VPPerson = None
        s: VPShape = None
        l: VPPolarity = None
        rule: VerbTenseRule = None
        for t in v.tense_rules:
            for p in v.tense_rules[t]:
                for s in v.tense_rules[t][p]:
                    for l in v.tense_rules[t][p][s]:
                        for rule in v.tense_rules[t][p][s][l]:
                            for form in v.tenses[rule.tense][rule.dependency][rule.person]:
                                particle = rule.particle
                                if rule.particle == '':
                                    gap = ''
                                else:
                                    gap = ' '
                                value = mutate(rule.mutation, form.value)
                                if rule.pronoun == '':
                                    gap2 = ''
                                else:
                                    gap2 = ' '
                                if check_nil(t, s, l, value):
                                    value = value.replace('fhuil', 'níl')
                                    particle = ''
                                    gap = ''
                                new_value = f'{particle}{gap}{value}{gap2}{rule.pronoun}'
                                self.tenses[t][s][p][l].append(Form(new_value))

        for pers in VPPerson:
            if pers == VPPerson.Any:
                continue
            has_synthetic = False
            for form in v.moods[VerbMood.Imper][PERSON_MAP[pers]]:
                pos = form.value
                neg = f'ná {mutate(Mutation.PrefH, form.value)}'
                self.moods[VPMood.Imper][pers][VPPolarity.Pos].append(Form(pos))
                self.moods[VPMood.Imper][pers][VPPolarity.Neg].append(Form(neg))
                has_synthetic = True

            if not has_synthetic or pers == VPPerson.Pl1 or pers == VPPerson.Pl3:
                for form in v.moods[VerbMood.Imper][VerbPerson.Base]:
                    pos = form.value + _PRONOUNS[pers]
                    neg = f'ná {mutate(Mutation.PrefH, form.value)}{_PRONOUNS[pers]}'
                    self.moods[VPMood.Imper][pers][VPPolarity.Pos].append(Form(pos))
                    self.moods[VPMood.Imper][pers][VPPolarity.Neg].append(Form(neg))
                    has_synthetic = True

        for pers in VPPerson:
            if pers == VPPerson.Any:
                continue
            pos_mut = Mutation.Ecl1
            neg_mut = Mutation.Len1
            neg_part = 'nár'

            if v.get_lemma == 'abair':
                neg_mut = Mutation.NoMut
            if v.get_lemma == 'bí':
                neg_part = 'ná'

            has_synthetic = False
            for form in v.moods[VerbMood.Subj][PERSON_MAP[pers]]:
                pos = f'go {mutate(pos_mut, form.value)}'
                neg = f'{neg_part} {mutate(neg_mut, form.value)}'
                self.moods[VPMood.Subj][pers][VPPolarity.Pos].append(Form(pos))
                self.moods[VPMood.Subj][pers][VPPolarity.Neg].append(Form(neg))
                has_synthetic = True

            if not has_synthetic or pers == VPPerson.Pl1:
                for form in v.moods[VerbMood.Subj][VerbPerson.Base]:
                    pos = f'go {mutate(pos_mut, form.value)}'
                    neg = f'{neg_part} {mutate(neg_mut, form.value)}'
                    self.moods[VPMood.Subj][pers][VPPolarity.Pos].append(Form(pos))
                    self.moods[VPMood.Subj][pers][VPPolarity.Neg].append(Form(neg))
                    has_synthetic = True

    def print_tense(self, tense, shape, pol) -> str:
        tmp = []
        for pers in VPPerson:
            if pers == VPPerson.Any:
                continue
            tmp.append(f'{pers.name}: [' + '] ['.join([f.value for f in self.tenses[tense][shape][pers][pol]]) + '] \n')
        return ''.join(tmp)

    def print_mood(self, mood, pol) -> str:
        tmp = []
        for pers in VPPerson:
            if pers == VPPerson.Any:
                continue
            tmp.append(f'{pers.name}: [' + '] ['.join([f.value for f in self.moods[mood][pers][pol]]) + '] \n')
        return ''.join(tmp)


_PRONOUNS = {
    VPPerson.Sg1: " mé",
    VPPerson.Sg2: " tú",
    VPPerson.Sg3Masc: " sé",
    VPPerson.Sg3Fem: " sí",
    VPPerson.Pl1: " muid",
    VPPerson.Pl2: " sibh",
    VPPerson.Pl3: " siad",
    VPPerson.NoSubject: "",
    VPPerson.Auto: ""
}


def init_tenses():
    """initialises the tenses dict."""
    tenses = {}
    for t in VPTense:
        if t == VPTense.Any:
            continue
        tenses[t] = {}
        for s in VPShape:
            if s == VPShape.Any:
                continue
            tenses[t][s] = {}
            for p in VPPerson:
                if p == VPPerson.Any:
                    continue
                tenses[t][s][p] = {}
                for pol in VPPolarity:
                    if pol == VPPolarity.Any:
                        continue
                    tenses[t][s][p][pol] = []
    return tenses


def init_moods():
    """initialises the moods dict."""
    moods = {}
    for m in VPMood:
        moods[m] = {}
        for p in VPPerson:
            if p == VPPerson.Any:
                continue
            moods[m][p] = {}
            for pol in VPPolarity:
                if pol == VPPolarity.Any:
                    continue
                moods[m][p][pol] = []
    return moods

from .attributes import VPPolarity, VPShape, VPTense
from .verb import init_moods, init_tenses, Verb
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
        def check_nil(t, s, l, value):
            a: bool = v.get_lemma == 'bí' 
            b: bool = t == VPTense.Pres
            c: bool = s == VPShape.Declar
            d: bool = l == VPPolarity.Neg
            e: bool = value.startswith('fhuil')
            return a and b and c and d and e
        for t in v.tense_rules:
            for p in v.tense_rules[t]:
                for s in v.tense_rules[t][p]:
                    for l in v.tense_rules[t][p][s]:
                        for rule in v.tense_rules[t][p][s][l]:
                            for form in v.tenses[rule.tense][rule.person][rule.dependency]:
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
                                self.tenses[t][p][s][l].append(Form(f'{particle}{gap}{value}{gap2}{rule.pronoun}'))

    def print(self) -> str:
        pass

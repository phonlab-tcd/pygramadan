from .attributes import Gender
from .forms import Form
from .opers import slenderise_target
from typing import List
import re

class SingularInfo():
    def __init__(self,
                 gender: Gender = None,
                 nominative: List[Form] = None,
                 genitive: List[Form] = None,
                 vocative: List[Form] = None,
                 dative: List[Form] = None) -> None:
        self.gender = gender
        self.nominative = nominative
        self.genitive = genitive
        self.vocative = vocative
        self.dative = dative

        if self.nominative is None:
            self.nominative = []
        if self.genitive is None:
            self.genitive = []
        if self.vocative is None:
            self.vocative = []
        if self.dative is None:
            self.dative = []


class SingularInfoO(SingularInfo):
    """Singular class O: all cases are identical."""
    def __init__(self, lemma: str = "", gender: Gender = None):
        super().__init__(gender=gender,
                         nominative=[Form(lemma)],
                         genitive=[Form(lemma)],
                         vocative=[Form(lemma)],
                         dative=[Form(lemma)])


class SingularInfoC(SingularInfo):
    """Singular class C: genitive and vocative formed by slenderisation."""
    def __init__(self,
                 lemma: str = "",
                 gender: Gender = None,
                 slenderisation_target: str = ""):
        super().__init__(gender=gender,
                         nominative=[Form(lemma)],
                         genitive=None,
                         vocative=None,
                         dative=[Form(lemma)])
        form = re.sub('ch$', 'gh', lemma)
        form = slenderise_target(form, slenderisation_target)
        if gender == Gender.Fem:
            self.vocative.append(Form(lemma))
            form = re.sub("igh$", "í", form)
            self.genitive.append(Form(form))
        else:
            self.vocative.append(Form(form))
            self.genitive.append(Form(form))



class SingularInfoL(SingularInfo):
    """Singular class L: genitive formed by broadening."""
    def __init__(self):
        pass

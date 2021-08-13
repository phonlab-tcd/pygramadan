from .attributes import Gender
from .forms import Form
from typing import List

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

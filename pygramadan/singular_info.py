from .attributes import Gender
from .forms import Form
from .opers import VOWELS, broaden, broaden_target, slenderise_target
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
    
    def __str__(self) -> str:
        return self.gramadan_string()

    def gramadan_string(self) -> str:
        nom = 'NOM: [' + '] ['.join([f.value for f in self.nominative]) + '] \n'
        gen = 'GEN: [' + '] ['.join([f.value for f in self.genitive]) + '] \n'
        voc = 'VOC: [' + '] ['.join([f.value for f in self.vocative]) + '] \n'
        dat = 'DAT: [' + '] ['.join([f.value for f in self.dative]) + '] \n'
        return nom + gen + voc + dat


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
    def __init__(self,
                 lemma: str = "",
                 gender: Gender = None,
                 slenderisation_target: str = ""):
        super().__init__(gender=gender,
                         nominative=[Form(lemma)],
                         genitive=None,
                         vocative=[Form(lemma)],
                         dative=[Form(lemma)])
        form = broaden_target(lemma, slenderisation_target)
        self.genitive.append(Form(form))


class SingularInfoE(SingularInfo):
    """Singular class E: genitive formed by suffix "-e"."""
    def __init__(self,
                 lemma: str = "",
                 gender: Gender = None,
                 syncope: bool = False,
                 double_dative: bool = False,
                 slenderisation_target: str = ""):
        super().__init__(gender=gender,
                         nominative=[Form(lemma)],
                         genitive=None,
                         vocative=[Form(lemma)],
                         dative=None)
        form = lemma
        if syncope:
            form = syncope(form)
        form = slenderise_target(form, slenderisation_target)
        self.dative.append(Form(form))
        if double_dative:
            self.dative.append(Form(lemma))
        form = re.sub(r"([" + VOWELS + "])ngt$", r"\1ngth", form)
        # original has 'ath', but must be 'aith' if 'e' is then appended
        form = re.sub(r'ú$', 'aith', form)
        form += 'e'
        self.genitive.append(Form(form))

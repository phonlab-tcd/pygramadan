from .attributes import Strength
from .forms import Form
from .opers import VOWELS, VOWELS_BROAD, VOWELS_SLENDER, broaden, broaden_target, slenderise_target, syncopate
from typing import List
import re


class PluralInfo():
    def __init__(self,
                 strength: Strength = None,
                 nominative: List[Form] = None,
                 genitive: List[Form] = None,
                 vocative: List[Form] = None) -> None:
        self.strength = strength
        self.nominative = nominative
        self.genitive = genitive
        self.vocative = vocative

        if self.nominative is None:
            self.nominative = []
        if self.genitive is None:
            self.genitive = []
        if self.vocative is None:
            self.vocative = []

    def __str__(self) -> str:
        return self.gramadan_string()

    def gramadan_string(self) -> str:
        nom = 'NOM: [' + '] ['.join([f.value for f in self.nominative]) + '] \n'
        gen = 'GEN: [' + '] ['.join([f.value for f in self.genitive]) + '] \n'
        voc = 'VOC: [' + '] ['.join([f.value for f in self.vocative]) + '] \n'
        return nom + gen + voc


class PluralInfoLgC(PluralInfo):
    """Plural class LgC: weak, plural formed by slenderisation."""
    def __init__(self, base: str, slenderisation_target: str = "") -> None:
        self.strength = Strength.Weak
        form = broaden(base)
        self.genitive.append(Form(form))
        form += 'a'
        self.vocative.append(Form(form))
        form = base
        form = re.sub('ch$', 'gh', form)
        form = slenderise_target(form, slenderisation_target)
        self.nominative.append(Form(form))
        pass
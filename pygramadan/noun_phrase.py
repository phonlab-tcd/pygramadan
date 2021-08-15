from pygramadan.attributes import Gender
from .forms import Form, FormSg
from typing import List


class NP():
    def __init__(self) -> None:
        self.disambig: str = ""
        self.sg_nom: List[FormSg] = []
        self.sg_gen: List[FormSg] = []
        self.sg_dat: List[FormSg] = []
        self.sg_nom_art: List[FormSg] = []
        self.sg_gen_art: List[FormSg] = []
        self.sg_dat_art_n: List[FormSg] = []
        self.sg_dat_art_s: List[FormSg] = []
        self.pl_nom: List[Form] = []
        self.pl_gen: List[Form] = []
        # this is odd, because Noun only has plural vocative
        self.pl_dat: List[Form] = []
        self.pl_nom_art: List[Form] = []
        self.pl_gen_art: List[Form] = []
        self.pl_dat_art: List[Form] = []

        self.is_definite = False
        self.is_immutable = False
        self.force_nominative = False

    def get_lemma(self) -> str:
        if len(self.sg_nom) != 0:
            return self.sg_nom[0].value
        elif len(self.sg_nom_art) != 0:
            return self.sg_nom_art[0].value
        elif len(self.pl_nom) != 0:
            return self.pl_nom[0].value
        elif len(self.pl_nom_art) != 0:
            return self.pl_nom_art[0].value
        else:
            raise Exception('get_lemma: no form found suitable for lemma')

    def get_identifier(self) -> str:
        disambig = ""
        if self.disambig != "":
            disambig = '_' + self.disambig
        return f"{self.get_lemma().replace(' ', '_')}_NP{disambig}"
    
    def has_gender(self) -> bool:
        return len(self.sg_nom) != 0 or len(self.sg_nom_art) != 0

    def get_gender(self) -> Gender:
        if len(self.sg_nom) != 0:
            return self.sg_nom[0].gender
        elif len(self.sg_nom_art) != 0:
            return self.sg_nom_art[0].gender
        else:
            return Gender.Masc

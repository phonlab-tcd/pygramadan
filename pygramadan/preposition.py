# coding=UTF-8
from typing import List
from .forms import Form

class Preposition:
    def __init__(self,
                 source,
                 lemma: str = "",
                 disambig: str = "",
                 sg1: List[Form] = [],
                 sg2: List[Form] = [],
                 sg3_masc: List[Form] = [],
                 sg3_fem: List[Form] = [],
                 pl1: List[Form] = [],
                 pl2: List[Form] = [],
                 pl2: List[Form] = []):
        self.lemma = lemma
        self.disambig = disambig
        self.sg1 = sg1
        self.sg2 = sg2
        self.sg3_masc = sg3_masc
        self.sg3_fem = sg3_fem
        self.pl1 = pl1
        self.pl2 = pl2
        self.pl3 = pl3

    def get_lemma():
        return self.lemma
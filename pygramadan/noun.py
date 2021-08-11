from .forms import Form, FormPlGen, FormSg
from .attributes import Gender, Strength
from typing import List

class Noun:
    def __str__(self) -> str:
        return '' +\
            'sgNom: [' + '] ['.join([f.value for f in self.sg_nom]) + '] \n' +\
            'sgGen: [' + '] ['.join([f.value for f in self.sg_gen]) + '] \n' +\
            'sgVoc: [' + '] ['.join([f.value for f in self.sg_voc]) + '] \n' +\
            'sgDat: [' + '] ['.join([f.value for f in self.sg_dat]) + '] \n' +\
            'plNom: [' + '] ['.join([f.value for f in self.pl_nom]) + '] \n' +\
            'plGen: [' + '] ['.join([f.value for f in self.pl_gen]) + '] \n' +\
            'plVoc: [' + '] ['.join([f.value for f in self.pl_voc]) + '] \n'

    def __init__(self, 
                 #file, 
                 definite: bool = False,
                 proper: bool = False,
                 immutable: bool = False,
                 article_genitive: bool = False,
                 disambig: str = "",
                 declension: int = 0,
                 sg_nom: List[FormSg] = [],
                 sg_gen: List[FormSg] = [],
                 sg_voc: List[FormSg] = [],
                 sg_dat: List[FormSg] = [],
                 pl_nom: List[Form] = [],
                 pl_gen: List[FormPlGen] = [],
                 pl_voc: List[Form] = [],
                 count: List[Form] = [],
                 ) -> None:
        self.is_definite: bool = definite
        self.is_proper: bool = proper
        self.is_immutable: bool = immutable
        self.article_genitive: bool = article_genitive

        self.disambig: str = disambig
        self.declension: int = declension

        self.sg_nom: list[FormSg] = sg_nom
        self.sg_gen: list[FormSg] = sg_gen
        self.sg_voc: list[FormSg] = sg_voc
        self.sg_dat: list[FormSg] = sg_dat
        self.pl_nom: list[Form] = pl_nom
        self.pl_gen: list[FormPlGen] = pl_gen
        self.pl_voc: list[Form] = pl_voc
        self.count: list[Form] = count
    
    def get_lemma(self) -> str:
        lemma_form = self.sg_nom[0]
        if lemma_form:
            return lemma_form.value
        else:
            return ""

    def get_gender(self) -> Gender:
        return self.sg_nom[0].gender


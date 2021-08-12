from typing import List
import xml.etree.ElementTree as ET
from forms import Form
from mutation import starts_vowel, starts_fthenvowel
from opers import mutate
from attributes import Mutation


class Adjective:
    def __init__(self,
                 source = None,
                 disambig: str = "",
                 declension: int = 0,
                 pfx: bool = False,
                 sg_nom: List[Form] = [],
                 sg_gen_masc: List[Form] = [],
                 sg_gen_fem: List[Form] = [],
                 sg_voc_masc: List[Form] = [],
                 sg_voc_fem: List[Form] = [],
                 pl_nom: List[Form] = [],
                 graded: List[Form] = [],
                 abstract: List[Form] = [],
                 ) -> None:
        self.disambig: str = disambig
        self.declension: int = declension
        self.prefix: bool = pfx

        self.sg_nom: list[Form] = sg_nom
        self.sg_gen_masc: list[Form] = sg_gen_masc
        self.sg_gen_fem: list[Form] = sg_gen_fem
        self.sg_voc_masc: list[Form] = sg_voc_masc
        self.sg_voc_fem: list[Form] = sg_voc_fem
        self.pl_nom: list[Form] = pl_nom
        self.graded: list[Form] = graded
        self.abstract: list[Form] = abstract

        if source is not None:
            self.from_xml(source)

    def get_lemma(self) -> str:
        lemma_form = self.full[0]
        if lemma_form:
            return lemma_form.value
        else:
            return ""

    def get_compar_pres(self) -> List[Form]:
        out = []
        for form in self.graded:
            out.append(Form("níos " + form.value))
        return out

    def get_super_pres(self) -> List[Form]:
        out = []
        for form in self.graded:
            out.append(Form("is " + form.value))
        return out

    def get_compar_past(self) -> List[Form]:
        out = []
        for form in self.graded:
            if starts_vowel(form.value):
                out.append(Form("ní b'" + form.value))
            elif starts_fthenvowel(form.value):
                mut = mutate(Mutation.Len1, form.value)
                out.append(Form("ní b'" + mut))
            else:
                mut = mutate(Mutation.Len1, form.value)
                out.append(Form("ní ba " + mut))
        return out

    def get_super_past(self) -> List[Form]:
        out = []
        for form in self.graded:
            if starts_vowel(form.value):
                out.append(Form("ab " + form.value))
            elif form.value[0:1] == 'f':
                mut = mutate(Mutation.Len1, form.value)
                out.append(Form("ab " + mut))
            else:
                mut = mutate(Mutation.Len1, form.value)
                out.append(Form("ba " + mut))
        return out

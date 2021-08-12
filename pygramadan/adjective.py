from typing import List
import xml.etree.ElementTree as ET
from forms import Form


class Adjective:
    def __init__(self,
                 source = None,
                 disambig: str = "",
                 declension: int = 0,
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

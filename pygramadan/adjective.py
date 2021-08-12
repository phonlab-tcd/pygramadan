# coding=UTF-8
from typing import List
import xml.etree.ElementTree as ET
from .forms import Form
from .mutation import starts_vowel, starts_fthenvowel
from .opers import mutate
from .attributes import Mutation


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
        lemma_form = self.sg_nom[0]
        if lemma_form:
            return lemma_form.value
        else:
            return ""

    def get_identifier(self) -> str:
        """
        Get an identifier for this adjective
        Note: called getNickname() in Gramadán
        """
        disambig = ""
        if self.disambig != "":
            disambig = "_" + self.disambig
        return f'{self.get_lemma().replace(" ", "_")}_{self.declension}{disambig}'

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

    def to_xml(self):
        props = {}
        props['default'] = self.get_lemma()
        props['declension'] = str(self.declension)
        props['disambig'] = self.disambig
        props['isPre'] = '1' if self.prefix else '0'
        root = ET.Element('adjective', props)
        for form in self.sg_nom:
            _ = ET.SubElement(root, 'sgNom', {'default': form.value})
        for form in self.sg_gen_masc:
            _ = ET.SubElement(root, 'sgGenMasc', {'default': form.value})
        for form in self.sg_gen_fem:
            _ = ET.SubElement(root, 'sgGenFem', {'default': form.value})
        for form in self.sg_voc_masc:
            _ = ET.SubElement(root, 'sgVocMasc', {'default': form.value})
        for form in self.sg_voc_fem:
            _ = ET.SubElement(root, 'sgVocFem', {'default': form.value})
        for form in self.pl_nom:
            _ = ET.SubElement(root, 'plNom', {'default': form.value})
        for form in self.graded:
            _ = ET.SubElement(root, 'graded', {'default': form.value})
        for form in self.abstract:
            _ = ET.SubElement(root, 'abstractNoun', {'default': form.value})

        return ET.tostring(root, encoding='UTF-8')

    def from_xml(self, source) -> None:
        tree = ET.parse(source)
        root = tree.getroot()

        self.is_definite = True if root.attrib['isDefinite'] == '1' else False
        self.prefix = True if root.attrib['isPre'] == '1' else False
        self.disambig = root.attrib['disambig']
        self.declension = int(root.attrib['declension'])

        for form in root.findall('./sgNom'):
            value = form.attrib.get('default')
            self.sg_nom.append(Form(value))
        for form in root.findall('./sgGenMasc'):
            value = form.attrib.get('default')
            self.sg_gen_masc.append(Form(value))
        for form in root.findall('./sgGenFem'):
            value = form.attrib.get('default')
            self.sg_gen_fem.append(Form(value))
        for form in root.findall('./sgVocMasc'):
            value = form.attrib.get('default')
            self.sg_voc_masc.append(Form(value))
        for form in root.findall('./sgVocFem'):
            value = form.attrib.get('default')
            self.sg_voc_fem.append(Form(value))
        for form in root.findall('./plNom'):
            value = form.attrib.get('default')
            self.pl_nom.append(Form(value))
        for form in root.findall('./graded'):
            value = form.attrib.get('default')
            self.graded.append(Form(value))
        for form in root.findall('./abstractNoun'):
            value = form.attrib.get('default')
            self.abstract.append(Form(value))


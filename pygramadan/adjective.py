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
                 dict = None,
                 disambig: str = "",
                 declension: int = 0,
                 pfx: bool = False,
                 sg_nom: List[Form] = None,
                 sg_gen_masc: List[Form] = None,
                 sg_gen_fem: List[Form] = None,
                 sg_voc_masc: List[Form] = None,
                 sg_voc_fem: List[Form] = None,
                 pl_nom: List[Form] = None,
                 graded: List[Form] = None,
                 abstract: List[Form] = None) -> None:
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

        if self.sg_nom is None:
            self.sg_nom = []
        if self.sg_gen_masc is None:
            self.sg_gen_masc = []
        if self.sg_gen_fem is None:
            self.sg_gen_fem = []
        if self.sg_voc_masc is None:
            self.sg_voc_masc = []
        if self.sg_voc_fem is None:
            self.sg_voc_fem = []
        if self.pl_nom is None:
            self.pl_nom = []
        if self.graded is None:
            self.graded = []
        if self.abstract is None:
            self.abstract = []

        if source is not None:
            self._empty()
            self.from_xml(source)
        elif dict is not None:
            self._empty()
            self._from_dict(dict)

    def _empty(self):
        self.disambig = ""
        self.declension = 0
        self.prefix = False
        self.sg_nom = []
        self.sg_gen_masc = []
        self.sg_gen_fem = []
        self.sg_voc_masc = []
        self.sg_voc_fem = []
        self.pl_nom = []
        self.graded = []
        self.abstract = []

    def _from_dict(self, dict) -> None:
        for key in ['sg_nom', 'sg_gen_masc', 'sg_gen_fem',
                    'sg_voc_masc', 'sg_voc_fem', 'pl_nom']:
            if key not in dict:
                raise Exception(f'Missing required key: {key}')
        if 'disambig' in dict:
            self.disambig = dict['disambig']
        self.sg_nom = [Form(dict['sg_nom'])]
        self.sg_gen_masc = [Form(dict['sg_gen_masc'])]
        self.sg_gen_fem = [Form(dict['sg_gen_fem'])]
        self.sg_voc_masc = [Form(dict['sg_voc_masc'])]
        self.sg_voc_fem = [Form(dict['sg_voc_fem'])]
        self.pl_nom = [Form(dict['pl_nom'])]
        if 'graded' in dict:
            self.graded = [Form(dict['graded'])]
        else:
            self.graded = []
        if 'abstract' in dict:
            self.abstract = [Form(dict['abstract'])]
        else:
            self.abstract = []

    def get_lemma(self) -> str:
        """Returns the adjective's lemma"""
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
        decl = str(self.declension) if self.declension > 0 else ""
        return f'{self.get_lemma().replace(" ", "_")}_adj{decl}{disambig}'

    def get_compar_pres(self) -> List[Form]:
        """
        Returns the present comparative forms of the adjective

        ...
        >>> beag = Adjective(source=sio)
        >>> beag.get_compar_pres()[0].value
        'níos lú'
        """
        out = []
        for form in self.graded:
            out.append(Form("níos " + form.value))
        return out

    def get_super_pres(self) -> List[Form]:
        """
        Returns the present superlative forms of the adjective

        ...
        >>> beag = Adjective(source=sio)
        >>> beag.get_super_pres()[0].value
        'is lú'
        """
        out = []
        for form in self.graded:
            out.append(Form("is " + form.value))
        return out

    def get_compar_past(self) -> List[Form]:
        """
        Returns the past comparative forms of the adjective

        ...
        >>> beag = Adjective(source=sio)
        >>> beag.get_compar_past()[0].value
        'ní ba lú'
        """
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
        """
        Returns the past superlative forms of the adjective

        ...
        >>> beag = Adjective(source=sio)
        >>> beag.get_super_past()[0].value
        'ba lú'
        """
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
        """Writes XML in BuNaMo format"""
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
        """
        Initialise from XML in BuNaMo format:

        >>> from pygramadan.adjective import Adjective
        >>> import io
        >>> xml = \"\"\"<adjective default="beag" declension="1" disambig="">
        ...   <sgNom default="beag" />
        ...   <sgGenMasc default="big" />
        ...   <sgGenFem default="bige" />
        ...   <plNom default="beaga" />
        ...   <graded default="lú" />
        ...   <abstractNoun default="laghad" />
        ... </adjective>\"\"\"
        >>> sio = io.StringIO(xml)
        >>> beag = Adjective(source=sio)
        """
        tree = ET.parse(source)
        root = tree.getroot()

        self.disambig = root.attrib['disambig']
        self.declension = int(root.attrib['declension'])
        if 'isPre' in root.attrib and root.attrib['isPre'] == '1':
            self.prefix = True
        else:
            self.prefix = False

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

    def get_all_forms(self, abstract = True):
        forms = set()
        for nom_sg in self.sg_nom:
            tpl = ('sg_nom', nom_sg.value)
            forms.add(tpl)
        for gen_sg_m in self.sg_gen_masc:
            tpl = ('sg_gen_masc', gen_sg_m.value)
            forms.add(tpl)
        for gen_sg_f in self.sg_gen_fem:
            tpl = ('sg_gen_fem', gen_sg_f.value)
            forms.add(tpl)
        for voc_sg_m in self.sg_voc_masc:
            tpl = ('sg_voc_masc', voc_sg_m.value)
            forms.add(tpl)
        for voc_sg_f in self.sg_voc_fem:
            tpl = ('sg_voc_fem', voc_sg_f.value)
            forms.add(tpl)
        for nom_pl in self.pl_nom:
            tpl = ('pl_nom', nom_pl.value)
            forms.add(tpl)
        for graded in self.graded:
            tpl = ('graded', graded.value)
            forms.add(tpl)
        if abstract:
            for abstract in self.abstract:
                tpl = ('abstract', abstract.value)
                forms.add(tpl)
        return list(forms)

    def get_unique_forms(self):
        return list(set([a[1] for a in self.get_all_forms()]))

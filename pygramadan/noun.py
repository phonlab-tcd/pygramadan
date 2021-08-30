# coding=UTF-8
from .forms import Form, FormPlGen, FormSg
from .attributes import Gender
from .xml_helpers import formsg_node, formpl_node, formplgen_node, write_sg, write_pl, write_pl_gen
from typing import List
import xml.etree.ElementTree as ET


class Noun:
    def __str__(self) -> str:
        return self._gramadan_string()

    def _gramadan_string(self) -> str:
        snom = 'sgNom: [' + '] ['.join([f.value for f in self.sg_nom]) + '] \n'
        sgen = 'sgGen: [' + '] ['.join([f.value for f in self.sg_gen]) + '] \n'
        svoc = 'sgVoc: [' + '] ['.join([f.value for f in self.sg_voc]) + '] \n'
        sdat = 'sgDat: [' + '] ['.join([f.value for f in self.sg_dat]) + '] \n'
        pnom = 'plNom: [' + '] ['.join([f.value for f in self.pl_nom]) + '] \n'
        pgen = 'plGen: [' + '] ['.join([f.value for f in self.pl_gen]) + '] \n'
        pvoc = 'plVoc: [' + '] ['.join([f.value for f in self.pl_voc]) + '] \n'
        return snom + sgen + svoc + sdat + pnom + pgen + pvoc

    def __init__(self,
                 source = None,
                 definite: bool = False,
                 proper: bool = False,
                 immutable: bool = False,
                 article_genitive: bool = False,
                 disambig: str = "",
                 declension: int = 0,
                 sg_nom: List[FormSg] = None,
                 sg_gen: List[FormSg] = None,
                 sg_voc: List[FormSg] = None,
                 sg_dat: List[FormSg] = None,
                 pl_nom: List[Form] = None,
                 pl_gen: List[FormPlGen] = None,
                 pl_voc: List[Form] = None,
                 count: List[Form] = None) -> None:
        self.is_definite: bool = definite
        self.is_proper: bool = proper
        self.is_immutable: bool = immutable
        self.article_genitive: bool = article_genitive
        # Keep track of generated "dative"
        self.artificial_dative = True

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

        if self.sg_nom is None:
            self.sg_nom = []
        if self.sg_gen is None:
            self.sg_gen = []
        if self.sg_voc is None:
            self.sg_voc = []
        if self.sg_dat is None:
            self.sg_dat = []
        if self.pl_nom is None:
            self.pl_nom = []
        if self.pl_gen is None:
            self.pl_gen = []
        if self.pl_voc is None:
            self.pl_voc = []
        if self.count is None:
            self.count = []

        if source is not None:
            self._empty()
            self.from_xml(source)

        self.add_dative()

    def _empty(self):
        """Clear the current contents"""
        self.is_definite = False
        self.is_proper = False
        self.is_immutable = False
        self.article_genitive = False

        self.disambig = ""
        self.declension = 0
        self.sg_nom = []
        self.sg_gen = []
        self.sg_voc = []
        self.sg_dat = []
        self.pl_nom = []
        self.pl_gen = []
        self.pl_voc = []
        self.count = []

    def get_lemma(self) -> str:
        lemma_form = self.sg_nom[0]
        if lemma_form:
            return lemma_form.value
        else:
            return ""

    def get_identifier(self) -> str:
        """
        Get an identifier for this noun
        Note: called getNickname() in Gramadán
        """
        gender = "fem" if self.get_gender() == Gender.Fem else "masc"
        disambig = ""
        if self.disambig != "":
            disambig = "_" + self.disambig
        outlem = self.get_lemma().replace(" ", "_")
        return f'{outlem}_{gender}_{self.declension}{disambig}'

    def get_gender(self) -> Gender:
        return self.sg_nom[0].gender

    def add_dative(self) -> None:
        if len(self.sg_dat) == 0:
            for form in self.sg_nom:
                self.sg_dat.append(FormSg(form.value, form.gender))
        self.artificial_dative = True

    def to_xml(self):
        props = {}
        props['default'] = self.get_lemma()
        props['declension'] = str(self.declension)
        props['disambig'] = self.disambig
        props['isProper'] = '1' if self.is_proper else '0'
        props['isDefinite'] = '1' if self.is_definite else '0'
        props['isImmutable'] = '1' if self.is_immutable else '0'
        props['allowArticledGenitive'] = '1' if self.article_genitive else '0'
        root = ET.Element('noun', props)

        write_sg(self.sg_nom, 'sgNom', root)
        write_sg(self.sg_gen, 'sgGen', root)
        if not self.artificial_dative:
            write_sg(self.sg_dat, 'sgDat', root)
        write_sg(self.sg_voc, 'sgVoc', root)
        write_pl(self.pl_nom, 'plNom', root)
        write_pl_gen(self.pl_gen, 'plGen', root)
        write_pl(self.pl_voc, 'plVoc', root)
        write_pl(self.count, 'count', root)

        return ET.tostring(root, encoding='UTF-8')

    def from_xml(self, source) -> None:
        """
        Initialise from XML in BuNaMo format:

        >>> from pygramadan.noun import Noun
        >>> import io
        >>> xml = \"\"\"<noun default="ainm" declension="4" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0">
        ...   <sgNom default="ainm" gender="masc" />
        ...   <sgGen default="ainm" gender="masc" />
        ...   <plNom default="ainmneacha" />
        ...   <plGen default="ainmneacha" strength="strong" />
        ... </noun>\"\"\"
        >>> sio = io.StringIO(xml)
        >>> ainm = Noun(source=sio)
        """
        tree = ET.parse(source)
        root = tree.getroot()

        self.is_definite = True if root.attrib['isDefinite'] == '1' else False
        self.is_proper = True if root.attrib['isProper'] == '1' else False
        if 'isImmutable' in root.attrib and root.attrib['isImmutable'] == '1':
            self.is_immutable = True
        else:
            self.is_immutable = False
        if 'allowArticledGenitive' in root.attrib and root.attrib['allowArticledGenitive'] == '1':
            self.article_genitive = True
        else:
            self.article_genitive = False
        self.disambig = root.attrib['disambig']
        self.declension = int(root.attrib['declension'])

        formsg_node(root, './sgNom', self.sg_nom)
        formsg_node(root, './sgGen', self.sg_gen)
        formsg_node(root, './sgVoc', self.sg_voc)
        formsg_node(root, './sgDat', self.sg_dat)
        if len(self.sg_dat) != 0:
            self.artificial_dative = False

        formpl_node(root, './plNom', self.pl_nom)
        formplgen_node(root, './plGen', self.pl_gen)
        formpl_node(root, './plVoc', self.pl_voc)
        formpl_node(root, './count', self.count)

    def get_all_forms(self, fake_dative = False):
        forms = set()
        for nom_sg in self.sg_nom:
            tpl = ('sg_nom', nom_sg.value)
            forms.add(tpl)
        for gen_sg in self.sg_gen:
            tpl = ('sg_gen', gen_sg.value)
            forms.add(tpl)
        for voc_sg in self.sg_voc:
            tpl = ('sg_voc', voc_sg.value)
            forms.add(tpl)
        for dat_sg in self.sg_dat:
            if not self.artificial_dative or fake_dative:
                tpl = ('sg_dat', dat_sg.value)
                forms.add(tpl)
        for nom_pl in self.pl_nom:
            tpl = ('pl_nom', nom_pl.value)
            forms.add(tpl)
        for gen_pl in self.pl_gen:
            tpl = ('pl_gen', gen_pl.value)
            forms.add(tpl)
        for voc_pl in self.pl_voc:
            tpl = ('pl_voc', voc_pl.value)
            forms.add(tpl)
        for count in self.count:
            tpl = ('count', count.value)
            forms.add(tpl)
        return list(forms)

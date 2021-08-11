from .forms import Form, FormPlGen, FormSg
from .attributes import Gender, Strength
from typing import List
import xml.etree.ElementTree as ET

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
                 source = None,
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

        if source != None:
            self.from_xml(source)

    def get_lemma(self) -> str:
        lemma_form = self.sg_nom[0]
        if lemma_form:
            return lemma_form.value
        else:
            return ""

    def get_gender(self) -> Gender:
        return self.sg_nom[0].gender

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
        for form in self.sg_nom:
            seprops = {}
            seprops['default'] = form.value
            seprops['gender'] = 'fem' if form.gender == Gender.Fem else 'masc'
            _ = ET.SubElement(root, 'sgNom', seprops)
        for form in self.sg_gen:
            seprops = {}
            seprops['default'] = form.value
            seprops['gender'] = 'fem' if form.gender == Gender.Fem else 'masc'
            _ = ET.SubElement(root, 'sgGen', seprops)
        for form in self.sg_dat:
            seprops = {}
            seprops['default'] = form.value
            seprops['gender'] = 'fem' if form.gender == Gender.Fem else 'masc'
            _ = ET.SubElement(root, 'sgDat', seprops)
        for form in self.sg_voc:
            seprops = {}
            seprops['default'] = form.value
            seprops['gender'] = 'fem' if form.gender == Gender.Fem else 'masc'
            _ = ET.SubElement(root, 'sgVoc', seprops)
        for form in self.pl_nom:
            seprops = {}
            seprops['default'] = form.value
            _ = ET.SubElement(root, 'plNom', seprops)
        for form in self.pl_gen:
            seprops = {}
            seprops['default'] = form.value
            seprops['strength'] = 'strong' if form.strength == Strength.Strong else 'weak'
            _ = ET.SubElement(root, 'plGen', seprops)
        for form in self.pl_voc:
            seprops = {}
            seprops['default'] = form.value
            _ = ET.SubElement(root, 'plVoc', seprops)
        for form in self.count:
            seprops = {}
            seprops['default'] = form.value
            _ = ET.SubElement(root, 'count', seprops)

        return ET.tostring(root, encoding='UTF-8')

    def from_xml(self, source) -> None:
        tree = ET.parse(source)
        root = tree.getroot()

        self.is_definite = True if root.attrib['isDefinite'] == '1' else False
        self.is_proper = True if root.attrib['isProper'] == '1' else False
        self.is_immutable = True if root.attrib['isImmutable'] == '1' else False
        self.article_genitive = True if root.attrib['allowArticledGenitive'] == '1' else False
        self.disambig = root.attrib['disambig']
        self.declension = int(root.attrib['declension'])

        for form in root.findall('./sgNom'):
            value = form.attrib.get('default')
            gender = Gender.Fem if form.attrib.get('gender') == 'fem' else Gender.Masc
            self.sg_nom.append(FormSg(value, gender))

        for form in root.findall('./sgGen'):
            value = form.attrib.get('default')
            gender = Gender.Fem if form.attrib.get('gender') == 'fem' else Gender.Masc
            self.sg_gen.append(FormSg(value, gender))

        for form in root.findall('./sgVoc'):
            value = form.attrib.get('default')
            gender = Gender.Fem if form.attrib.get('gender') == 'fem' else Gender.Masc
            self.sg_voc.append(FormSg(value, gender))

        for form in root.findall('./sgDat'):
            value = form.attrib.get('default')
            gender = Gender.Fem if form.attrib.get('gender') == 'fem' else Gender.Masc
            self.sg_dat.append(FormSg(value, gender))

        for form in root.findall('./plNom'):
            value = form.attrib.get('default')
            self.pl_nom.append(Form(value))

        for form in root.findall('./sgDat'):
            value = form.attrib.get('default')
            strength = Strength.Strong if form.attrib.get('strength') == 'strong' else Strength.Weak
            self.pl_gen.append(FormPlGen(value, strength))

        for form in root.findall('./plVoc'):
            value = form.attrib.get('default')
            self.pl_voc.append(Form(value))

        for form in root.findall('./count'):
            value = form.attrib.get('default')
            self.count.append(Form(value))

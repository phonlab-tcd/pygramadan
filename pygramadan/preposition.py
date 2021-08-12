# coding=UTF-8
from typing import List
from .forms import Form
import xml.etree.ElementTree as ET

class Preposition:
    def __init__(self,
                 source = None,
                 lemma: str = "",
                 disambig: str = "",
                 sg1: List[Form] = None,
                 sg2: List[Form] = None,
                 sg3_masc: List[Form] = None,
                 sg3_fem: List[Form] = None,
                 pl1: List[Form] = None,
                 pl2: List[Form] = None,
                 pl3: List[Form] = None):
        self.lemma: str = lemma
        self.disambig: str = disambig
        self.sg1: List[Form] = sg1
        self.sg2: List[Form] = sg2
        self.sg3_masc: List[Form] = sg3_masc
        self.sg3_fem: List[Form] = sg3_fem
        self.pl1: List[Form] = pl1
        self.pl2: List[Form] = pl2
        self.pl3: List[Form] = pl3

        if self.sg1 is None:
            self.sg1 = []
        if self.sg2 is None:
            self.sg2 = []
        if self.sg3_masc is None:
            self.sg3_masc = []
        if self.sg3_fem is None:
            self.sg3_fem = []
        if self.pl1 is None:
            self.pl1 = []
        if self.pl2 is None:
            self.pl2 = []
        if self.pl3 is None:
            self.pl3 = []

        if source is not None:
            self.from_xml(source)

    def get_identifier(self) -> str:
        """
        Get an identifier for this preposition
        Note: called getNickname() in Gramadán
        """
        disambig = ""
        if self.disambig != "":
            disambig = "_" + self.disambig
        return f'{self.get_lemma().replace(" ", "_")}_prep{disambig}'

    def is_empty(self) -> bool:
        total = len(self.sg1)
        total += len(self.sg2)
        total += len(self.sg3_masc)
        total += len(self.sg3_fem)
        total += len(self.pl1)
        total += len(self.pl2)
        total += len(self.pl3)
        return (total == 0)

    def get_lemma(self):
        return self.lemma

    def to_xml(self):
        props = {}
        props['default'] = self.get_lemma()
        props['disambig'] = self.disambig
        root = ET.Element('preposition', props)
        for form in self.sg1:
            _ = ET.SubElement(root, 'sg1', {'default': form.value})
        for form in self.sg2:
            _ = ET.SubElement(root, 'sg2', {'default': form.value})
        for form in self.sg3_masc:
            _ = ET.SubElement(root, 'sg3Masc', {'default': form.value})
        for form in self.sg3_fem:
            _ = ET.SubElement(root, 'sg3Fem', {'default': form.value})
        for form in self.pl1:
            _ = ET.SubElement(root, 'pl1', {'default': form.value})
        for form in self.pl2:
            _ = ET.SubElement(root, 'pl2', {'default': form.value})
        for form in self.pl3:
            _ = ET.SubElement(root, 'pl3', {'default': form.value})

        return ET.tostring(root, encoding='UTF-8')

    def from_xml(self, source) -> None:
        tree = ET.parse(source)
        root = tree.getroot()

        self.lemma = root.attrib['default']
        self.disambig = root.attrib['disambig']

        for form in root.findall('./sg1'):
            value = form.attrib.get('default')
            self.sg1.append(Form(value))
        for form in root.findall('./sg2'):
            value = form.attrib.get('default')
            self.sg2.append(Form(value))
        for form in root.findall('./sg3Masc'):
            value = form.attrib.get('default')
            self.sg3_masc.append(Form(value))
        for form in root.findall('./sg3Fem'):
            value = form.attrib.get('default')
            self.sg3_fem.append(Form(value))
        for form in root.findall('./pl1'):
            value = form.attrib.get('default')
            self.pl1.append(Form(value))
        for form in root.findall('./pl2'):
            value = form.attrib.get('default')
            self.pl2.append(Form(value))
        for form in root.findall('./pl3'):
            value = form.attrib.get('default')
            self.pl3.append(Form(value))

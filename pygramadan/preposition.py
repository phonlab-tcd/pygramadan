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
        """
        Initialise from XML in BuNaMo format:

        >>> from pygramadan.preposition import Preposition
        >>> import io
        >>> xml = \"\"\"<preposition default="le" disambig="">
        ...   <sg1 default="liom" />
        ...   <sg2 default="leat" />
        ...   <sg3Masc default="leis" />
        ...   <sg3Fem default="léi" />
        ...   <pl1 default="linn" />
        ...   <pl2 default="libh" />
        ...   <pl3 default="leo" />
        ... </preposition>\"\"\"
        >>> sio = io.StringIO(xml)
        >>> le = Preposition(source=sio)
        """
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

    def get_all_forms(self):
        """
        Returns a list of tuples, `(person-form, form)`:

        >>> le.get_all_forms()
        [('pl2', 'libh'), ('sg3_masc', 'leis'), ('sg1', 'linn'), ('pl3', 'leo'), ('sg2', 'leat'), ('sg1', 'liom'), ('sg3_fem', 'léi')]
        """
        forms = set()
        for sg1 in self.sg1:
            tpl = ('sg1', sg1.value)
            forms.add(tpl)
        for sg2 in self.sg2:
            tpl = ('sg2', sg2.value)
            forms.add(tpl)
        for sg3_masc in self.sg3_masc:
            tpl = ('sg3_masc', sg3_masc.value)
            forms.add(tpl)
        for sg3_fem in self.sg3_fem:
            tpl = ('sg3_fem', sg3_fem.value)
            forms.add(tpl)
        for pl1 in self.pl1:
            tpl = ('sg1', pl1.value)
            forms.add(tpl)
        for pl2 in self.pl2:
            tpl = ('pl2', pl2.value)
            forms.add(tpl)
        for pl3 in self.pl3:
            tpl = ('pl3', pl3.value)
            forms.add(tpl)
        return list(forms)

    def get_unique_forms(self):
        """
        Returns a list of unique word forms:

        >>> le.get_unique_forms()
        ['léi', 'liom', 'leo', 'leis', 'libh', 'linn', 'leat']
        """
        return list(set([a[1] for a in self.get_all_forms()]))


def get_example() -> str:
    return """\
<preposition default="le" disambig="">
  <sg1 default="liom" />
  <sg2 default="leat" />
  <sg3Masc default="leis" />
  <sg3Fem default="léi" />
  <pl1 default="linn" />
  <pl2 default="libh" />
  <pl3 default="leo" />
</preposition>
"""

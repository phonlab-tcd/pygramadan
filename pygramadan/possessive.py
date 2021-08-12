from typing import List
import xml.etree.ElementTree as ET
from .attributes import Mutation
from .forms import Form

_MUT = {
    "none": Mutation.NoMut,
    "len1": Mutation.Len1,
    "len2": Mutation.Len2,
    "len3": Mutation.Len3,
    "ecl1": Mutation.Ecl1,
    "ecl1x": Mutation.Ecl1x,
    "ecl2": Mutation.Ecl2,
    "ecl3": Mutation.Ecl3,
    "prefT": Mutation.PrefT,
    "prefH": Mutation.PrefH,
    "len1D": Mutation.Len1D,
    "len2D": Mutation.Len2D,
    "len3D": Mutation.Len3D
}


def _lcfirst(text):
    return text[0:1].lower() + text[1:]


class Possessive:
    def __init__(self,
                 source = None,
                 disambig: str = "",
                 mutation: Mutation = Mutation.NoMut,
                 full: List[Form] = None,
                 apos: List[Form] = None,
                 ) -> None:
        self.disambig: bool = disambig
        self.mutation: Mutation = mutation

        self.full: list[Form] = full
        self.apos: list[Form] = apos

        if source is not None:
            self.from_xml(source)

        if self.full is None:
            self.full = []
        if self.apos is None:
            self.apos = []

    def get_lemma(self) -> str:
        lemma_form = self.full[0]
        if lemma_form:
            return lemma_form.value
        else:
            return ""

    def get_identifier(self) -> str:
        """
        Get an identifier for this possessive
        Note: called getNickname() in Gramadán
        """
        disambig = ""
        if self.disambig != "":
            disambig = "_" + self.disambig
        return f'{self.get_lemma().replace(" ", "_")}{disambig}_poss'

    def to_xml(self):
        props = {}
        props['default'] = self.get_lemma()
        props['disambig'] = self.disambig
        props['mutation'] = _lcfirst(self.mutation.__str__())
        root = ET.Element('possessive', props)
        for form in self.full:
            _ = ET.SubElement(root, 'full', {'default': form.value})
        for form in self.apos:
            _ = ET.SubElement(root, 'apos', {'default': form.value})

        return ET.tostring(root, encoding='UTF-8')

    def from_xml(self, source) -> None:
        tree = ET.parse(source)
        root = tree.getroot()

        self.disambig = root.attrib['disambig']
        mutname = root.attrib['mutation']
        self.mutation = _MUT.get(mutname)

        for form in root.findall('./full'):
            value = form.attrib.get('default')
            self.full.append(Form(value))

        for form in root.findall('./apos'):
            value = form.attrib.get('default')
            self.apos.append(Form(value))

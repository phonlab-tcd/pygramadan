from typing import List
import xml.etree.ElementTree as ET
from attributes import Mutation

_MUT = {
    "none": Mutation.NoMut,
    "len1": Mutation.Len1,
    "len2": Mutation.Len2,
    "len3": Mutation.Len3,
    "ecl1": Mutation.Ecl1,
    "ecl1x": Mutation.Ecl1x,
    "ecl2": Mutation.Ecl2,
    "ecl3": Mutation.Ecl3,
    "preft": Mutation.PrefT,
    "prefh": Mutation.PrefH,
    "len1d": Mutation.Len1D,
    "len2d": Mutation.Len2D,
    "len3d": Mutation.Len3D
}


class Possessive:
    def get_lemma(self) -> str:
        lemma_form = self.full[0]
        if lemma_form:
            return lemma_form.value
        else:
            return ""

    def to_xml(self):
        props = {}
        props['default'] = self.get_lemma()
        props['disambig'] = self.disambig
        props['mutation'] = self.mutation.__str__().lower()
        root = ET.Element('possessive', props)
        for form in self.full:
            _ = ET.SubElement(root, 'full', {'default': form.value})
        for form in self.apos:
            _ = ET.SubElement(root, 'apos', {'default': form.value})

        return ET.tostring(root, encoding='UTF-8')

from typing import List
import xml.etree.ElementTree as ET
from .noun import Noun
from .noun_phrase import NP


class PrinterNeid:
    def __init__(self) -> None:
        self.with_xml_declaration = False

    def print_noun_xml(self, n: Noun) -> str:
        np = NP(n)

        props = {}
        props['lemma'] = n.get_lemma()
        props['uid'] = n.get_identifier()
        root = ET.Element('Lemma', props)

        xsl = ET.PI('xml-stylesheet', "type='text/xsl' href='!gram.xsl'")

        nprops = {}
        nprops['gender'] = n.get_gender().name.lower()
        nprops['declension'] = str(n.declension)
        ntag = ET.SubElement(root, 'noun', nprops)
        for sng in zip(np.sg_nom, np.sg_nom_art):
            grouptag = ET.SubElement(ntag, 'sgNom')
            artn = ET.SubElement(grouptag, 'articleNo')
            artn.text = sng[0].value
            arty = ET.SubElement(grouptag, 'articleYes')
            arty.text = sng[1].value

        return ET.tostring(root, encoding='UTF-8')

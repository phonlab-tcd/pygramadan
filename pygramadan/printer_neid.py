from typing import List
import xml.etree.ElementTree as ET
from .noun import Noun


class PrinterNeid:
    def __init__(self) -> None:
        self.with_xml_declaration = False

    def print_noun_xml(self, n: Noun) -> str:
        props = {}
        props['lemma'] = n.get_lemma()
        props['uid'] = n.get_identifier()
        root = ET.Element('Lemma', props)

        xsl = ET.PI('xml-stylesheet', "type='text/xsl' href='!gram.xsl'")

        nprops = {}
        nprops['gender'] = n.get_gender().name.lower()


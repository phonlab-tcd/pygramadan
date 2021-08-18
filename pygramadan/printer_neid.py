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
        def _do_element(noun_tag, lista, listb, name):
            for sng in zip(lista, listb):
                grouptag = ET.SubElement(noun_tag, name)
                artn = ET.SubElement(grouptag, 'articleNo')
                artn.text = sng[0].value
                arty = ET.SubElement(grouptag, 'articleYes')
                arty.text = sng[1].value
        _do_element(ntag, np.sg_nom, np.sg_nom_art, 'sgNom')
        _do_element(ntag, np.sg_gen, np.sg_gen_art, 'sgGen')
        _do_element(ntag, np.pl_nom, np.pl_nom_art, 'plNom')
        _do_element(ntag, np.pl_gen, np.pl_gen_art, 'plGen')

        return ET.tostring(root, encoding='UTF-8')

from .mutation import starts_vowel
from .opers import mutate
from .attributes import Mutation
from .adjective import Adjective
from .noun import Noun
from .noun_phrase import NP
from .prepositional_phrase import PP
from typing import List
import xml.etree.ElementTree as ET



DCL = ET.PI('xml', "version='1.0' encoding='utf-8'")
XSL = ET.PI('xml-stylesheet', "type='text/xsl' href='!gram.xsl'")
NL = bytes('\n', encoding='UTF-8')


class PrinterNeid:
    def __init__(self, with_xml_declarations = True) -> None:
        self.with_xml_declarations = with_xml_declarations

    def print_noun_xml(self, n: Noun) -> str:
        np = NP(n)

        props = {}
        props['lemma'] = n.get_lemma()
        props['uid'] = n.get_identifier()
        root = ET.Element('Lemma', props)

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

        out = ET.tostring(root, encoding='UTF-8')
        if self.with_xml_declarations:
            return ET.tostring(DCL) + NL + ET.tostring(XSL) + NL + out
        else:
            return out

    def print_np_xml(self, np: NP) -> str:
        props = {}
        props['lemma'] = np.get_lemma()
        props['uid'] = np.get_identifier()
        root = ET.Element('Lemma', props)

        nprops = {}
        nprops['gender'] = np.get_gender().name.lower()
        nprops['forceNominative'] = '1' if np.force_nominative else '0'
        ntag = ET.SubElement(root, 'nounPhrase', nprops)
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

        out = ET.tostring(root, encoding='UTF-8')
        if self.with_xml_declarations:
            return ET.tostring(DCL) + NL + ET.tostring(XSL) + NL + out
        else:
            return out

    def print_adjective(self, adj: Adjective) -> str:
        props = {}
        props['lemma'] = adj.get_lemma()
        props['uid'] = adj.get_identifier()
        root = ET.Element('Lemma', props)

        aprops = {}
        aprops['declension'] = str(adj.declension)
        atag = ET.SubElement(root, 'adjective', aprops)

        def _do_tags(root, list, name, mut):
            for sub in list:
                subtag = ET.SubElement(root, name)
                subtag.text = mutate(mut, sub.value)
        _do_tags(atag, adj.sg_nom, 'sgNomMasc', Mutation.NoMut)
        _do_tags(atag, adj.sg_nom, 'sgNomFem', Mutation.Len1)
        _do_tags(atag, adj.sg_gen_masc, 'sgGenMasc', Mutation.Len1)
        _do_tags(atag, adj.sg_gen_fem, 'sgGenFem', Mutation.NoMut)
        _do_tags(atag, adj.pl_nom, 'plNom', Mutation.NoMut)
        _do_tags(atag, adj.pl_nom, 'plNomSlen', Mutation.Len1)
        _do_tags(atag, adj.pl_nom, 'plGenStrong', Mutation.NoMut)
        _do_tags(atag, adj.sg_nom, 'plGenWeak', Mutation.NoMut)
        for form in adj.get_compar_pres():
            subtag = ET.SubElement(atag, 'comparPres')
            subtag.text = form.value
        for form in adj.get_compar_past():
            subtag = ET.SubElement(atag, 'comparPast')
            subtag.text = form.value
        for form in adj.get_super_pres():
            subtag = ET.SubElement(atag, 'superPres')
            subtag.text = form.value
        for form in adj.get_super_past():
            subtag = ET.SubElement(atag, 'superPast')
            subtag.text = form.value
        for form in adj.abstract:
            subtag = ET.SubElement(atag, 'abstractNoun')
            subtag.text = form.value
        for form in adj.abstract:
            subtag = ET.SubElement(atag, 'abstractNounExamples')
            ssubtag1 = ET.SubElement(subtag, 'example')
            ssubtag1.text = "dá " + mutate(Mutation.Len1, form.value)
            ssubtag2 = ET.SubElement(subtag, 'example')
            if starts_vowel(form.value):
                ssubtag2.text = "ag dul in " + mutate(Mutation.NoMut, form.value)
            else:
                ssubtag2.text = "ag dul i " + mutate(Mutation.Ecl1, form.value)

        out = ET.tostring(root, encoding='UTF-8')
        if self.with_xml_declarations:
            return ET.tostring(DCL) + NL + ET.tostring(XSL) + NL + out
        else:
            return out

    def print_pp_xml(self, pp: PP) -> str:
        props = {}
        props['lemma'] = pp.get_lemma()
        props['uid'] = pp.get_identifier()
        root = ET.Element('Lemma', props)

        ntag = ET.SubElement(root, 'prepositionalPhrase')
        for sng in zip(pp.sg, pp.sg_art_n, pp.sg_art_s):
            grouptag = ET.SubElement(ntag, 'sg')
            artn = ET.SubElement(grouptag, 'articleNo')
            artn.text = sng[0].value
            if sng[1].value == sng[2].value:
                arty = ET.SubElement(grouptag, 'articleYes')
                arty.text = sng[1].value
            else:
                artyn = ET.SubElement(grouptag, 'articleYes', {'var': 'north'})
                artyn.text = sng[1].value
                artys = ET.SubElement(grouptag, 'articleYes', {'var': 'south'})
                artys.text = sng[2].value

        for plr in zip(pp.pl, pp.pl_art):
            grouptag = ET.SubElement(ntag, 'pl')
            artn = ET.SubElement(grouptag, 'articleNo')
            artn.text = plr[0].value
            arty = ET.SubElement(grouptag, 'articleYes')
            arty.text = plr[1].value

        out = ET.tostring(root, encoding='UTF-8')
        if self.with_xml_declarations:
            return ET.tostring(DCL) + NL + ET.tostring(XSL) + NL + out
        else:
            return out

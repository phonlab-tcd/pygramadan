# coding=UTF-8
from pygramadan.noun import Noun
from pygramadan.wiktionary_inflection import noun_f3, noun_m4
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
import io


FEOIL_XML = """
<noun default="feoil" declension="3" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="feoil" gender="fem" />
  <sgGen default="feola" gender="fem" />
  <plNom default="feolta" />
  <plGen default="feolta" strength="strong" />
</noun>
"""


FEOIL_WIKI = "{{ga-decl-f3|f|eoil|eola|eolta}}"


def test_noun_f3():
    sio = io.StringIO(FEOIL_XML)
    feoil_xml = Noun(source=sio)
    feoil_wiki = noun_f3(FEOIL_WIKI)
    assert feoil_xml.get_lemma() == feoil_wiki.get_lemma()
    assert feoil_xml.get_gender() == feoil_wiki.get_gender()
    assert len(feoil_xml.pl_gen) == len(feoil_wiki.pl_gen)
    assert feoil_xml.pl_gen[0].value == feoil_wiki.pl_gen[0].value
    assert feoil_xml.pl_gen[0].strength == feoil_wiki.pl_gen[0].strength


PANDA_XML = """
<noun default="panda" declension="4" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="panda" gender="masc" />
  <sgGen default="panda" gender="masc" />
  <plNom default="pandaí" />
  <plGen default="pandaí" strength="strong" />
</noun>
"""


PANDA_WIKI = "{{ga-decl-m4|p|anda|andaí}}"


def test_noun_m4():
    sio = io.StringIO(PANDA_XML)
    panda_xml = Noun(source=sio)
    panda_wiki = noun_m4(PANDA_WIKI)
    assert panda_xml.get_lemma() == panda_wiki.get_lemma()
    assert panda_xml.get_gender() == panda_wiki.get_gender()
    assert len(panda_xml.pl_gen) == len(panda_wiki.pl_gen)
    assert panda_xml.pl_gen[0].value == panda_wiki.pl_gen[0].value
    assert panda_xml.pl_gen[0].strength == panda_wiki.pl_gen[0].strength

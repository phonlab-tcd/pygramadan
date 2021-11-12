# coding=UTF-8
from pygramadan.noun import Noun
from pygramadan.wiktionary_inflection import noun_f2, noun_f3, noun_m4, noun_f5, split_tpl_params
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
import io
from pytest import raises


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


def test_split_tpl_params():
    o1 = split_tpl_params("{{name|a|b|c}}")
    assert o1["name"] == "name"
    assert len(o1["positional"]) == 3
    assert o1["positional"][-1] == "c"
    o2 = split_tpl_params("{{name|a|b|c|n=foo}}")
    assert o2["name"] == "name"
    assert len(o2["positional"]) == 3
    assert o2["positional"][-1] == "c"
    assert o2["n"] == "foo"
    with raises(Exception) as e_info:
        o3 = split_tpl_params("{{name|a|b|c|n=foo|d}}")


LONG_XML = """
<noun default="long" declension="2" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="long" gender="fem" />
  <sgGen default="loinge" gender="fem" />
  <sgDat default="loing" gender="fem" />
  <plNom default="longa" />
  <plGen default="long" strength="weak" />
</noun>
"""


LONG_WIKI = "{{ga-decl-f2|l|ong|oinge|dat=oing|datoc=a}}"


def test_noun_m4():
    sio = io.StringIO(LONG_XML)
    long_xml = Noun(source=sio)
    long_wiki = noun_f2(LONG_WIKI)
    assert long_xml.get_lemma() == long_wiki.get_lemma()
    assert long_xml.get_gender() == long_wiki.get_gender()
    assert len(long_xml.pl_gen) == len(long_wiki.pl_gen)
    assert long_xml.pl_gen[0].value == long_wiki.pl_gen[0].value
    assert long_xml.pl_gen[0].value == long_wiki.pl_gen[0].value
    assert long_xml.pl_gen[0].strength == long_wiki.pl_gen[0].strength
    assert long_xml.sg_dat[0].value == long_wiki.sg_dat[0].value


CAORA_XML = """
<noun default="caora" declension="5" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="caora" gender="fem" />
  <sgGen default="caorach" gender="fem" />
  <plNom default="caoirigh" />
  <plGen default="caorach" strength="weak" />
</noun>
"""


CAORA_WIKI = "{{ga-decl-f5|c|aora|aorach|aoirigh|genpl=aorach}}"


def test_noun_f5():
    sio = io.StringIO(CAORA_XML)
    caora_xml = Noun(source=sio)
    caora_wiki = noun_f5(CAORA_WIKI)
    assert caora_xml.get_lemma() == caora_wiki.get_lemma()
    assert caora_xml.get_gender() == caora_wiki.get_gender()
    assert len(caora_xml.pl_gen) == len(caora_wiki.pl_gen)
    assert caora_xml.pl_gen[0].value == caora_wiki.pl_gen[0].value
    assert caora_xml.pl_gen[0].value == caora_wiki.pl_gen[0].value
    assert caora_xml.pl_gen[0].strength == caora_wiki.pl_gen[0].strength

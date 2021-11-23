# coding=UTF-8
from pygramadan.noun import Noun
from pygramadan.wiktionary_inflection import noun_f2, noun_f3, noun_m1, noun_m4, noun_f5, split_tpl_params
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


TOIL_XML = """
<noun default="toil" declension="3" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="toil" gender="fem" />
  <sgGen default="tola" gender="fem" />
</noun>
"""


TOIL_WIKI = "{{ga-decl-f3-nopl|t|oil|ola}}"


def test_noun_f3():
    sio = io.StringIO(FEOIL_XML)
    feoil_xml = Noun(source=sio)
    feoil_wiki = noun_f3(FEOIL_WIKI)
    assert feoil_xml.get_lemma() == feoil_wiki.get_lemma()
    assert feoil_xml.get_gender() == feoil_wiki.get_gender()
    assert len(feoil_xml.pl_gen) == len(feoil_wiki.pl_gen)
    assert feoil_xml.pl_gen[0].value == feoil_wiki.pl_gen[0].value
    assert feoil_xml.pl_gen[0].strength == feoil_wiki.pl_gen[0].strength

    sio = io.StringIO(TOIL_XML)
    toil_xml = Noun(source=sio)
    toil_wiki = noun_f3(TOIL_WIKI)
    assert toil_xml.get_lemma() == toil_wiki.get_lemma()
    assert toil_xml.get_gender() == toil_wiki.get_gender()
    assert len(toil_xml.pl_gen) == len(toil_wiki.pl_gen) == 0


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


SAIL_XML = """
<noun default="sail" declension="2" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="sail" gender="fem" />
  <sgGen default="saile" gender="fem" />
</noun>
"""


SAIL_WIKI = "{{ga-decl-f2-nopl|sa|il|ile}}"


def test_noun_f2():
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

    sio = io.StringIO(SAIL_XML)
    sail_xml = Noun(source=sio)
    sail_wiki = noun_f2(SAIL_WIKI)
    assert sail_xml.get_lemma() == sail_wiki.get_lemma()
    assert sail_xml.get_gender() == sail_wiki.get_gender()
    assert len(sail_xml.pl_gen) == len(sail_wiki.pl_gen) == 0


CAORA_XML = """
<noun default="caora" declension="5" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="caora" gender="fem" />
  <sgGen default="caorach" gender="fem" />
  <plNom default="caoirigh" />
  <plGen default="caorach" strength="weak" />
</noun>
"""


CAORA_WIKI = "{{ga-decl-f5|c|aora|aorach|aoirigh|genpl=aorach}}"


MEANMA_XML = """
<noun default="meanma" declension="5" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="meanma" gender="fem" />
  <sgGen default="meanman" gender="fem" />
</noun>
"""


MEANMA_WIKI = "{{ga-decl-f5-nopl|m|eanma|eanman}}"


def test_noun_f5():
    sio = io.StringIO(CAORA_XML)
    meanma_xml = Noun(source=sio)
    meanma_wiki = noun_f5(CAORA_WIKI)
    assert meanma_xml.get_lemma() == meanma_wiki.get_lemma()
    assert meanma_xml.get_gender() == meanma_wiki.get_gender()
    assert len(meanma_xml.pl_gen) == len(meanma_wiki.pl_gen)
    assert meanma_xml.pl_gen[0].value == meanma_wiki.pl_gen[0].value
    assert meanma_xml.pl_gen[0].value == meanma_wiki.pl_gen[0].value
    assert meanma_xml.pl_gen[0].strength == meanma_wiki.pl_gen[0].strength

    sio = io.StringIO(MEANMA_XML)
    meanma_xml = Noun(source=sio)
    meanma_wiki = noun_f5(MEANMA_WIKI)
    assert meanma_xml.get_lemma() == meanma_wiki.get_lemma()
    assert meanma_xml.get_gender() == meanma_wiki.get_gender()
    assert len(meanma_xml.pl_gen) == len(meanma_wiki.pl_gen) == 0


BAS_XML = """
<noun default="bás" declension="1" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="bás" gender="masc" />
  <sgGen default="báis" gender="masc" />
  <plNom default="básanna" />
  <plGen default="básanna" strength="strong" />
</noun>
"""


BAS_WIKI = "{{ga-decl-m1|b|ás|áis|pl=ásanna|strong=yes}}"


ULL_XML = """
<noun default="úll" declension="1" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="úll" gender="masc" />
  <sgGen default="úill" gender="masc" />
  <plNom default="úlla" />
  <plGen default="úll" strength="weak" />
</noun>
"""


ULL_WIKI = "{{ga-decl-m1|ú|ll|ill|pl=lla}}"


def test_noun_m1():
    sio = io.StringIO(BAS_XML)
    bas_xml = Noun(source=sio)
    bas_wiki = noun_m1(BAS_WIKI)
    assert bas_xml.get_lemma() == bas_wiki.get_lemma()
    assert bas_xml.get_gender() == bas_wiki.get_gender()
    assert len(bas_xml.pl_gen) == len(bas_wiki.pl_gen)
    assert bas_xml.pl_gen[0].value == bas_wiki.pl_gen[0].value
    assert bas_xml.pl_gen[0].strength == bas_wiki.pl_gen[0].strength
    assert bas_xml.pl_nom[0].value == bas_wiki.pl_nom[0].value

    sio = io.StringIO(ULL_XML)
    ull_xml = Noun(source=sio)
    ull_wiki = noun_m1(ULL_WIKI)
    assert ull_xml.get_lemma() == ull_wiki.get_lemma()
    assert ull_xml.get_gender() == ull_wiki.get_gender()
    assert len(ull_xml.pl_gen) == len(ull_wiki.pl_gen)
    assert ull_xml.pl_gen[0].value == ull_wiki.pl_gen[0].value
    assert ull_xml.pl_gen[0].strength == ull_wiki.pl_gen[0].strength
    assert ull_xml.pl_nom[0].value == ull_wiki.pl_nom[0].value

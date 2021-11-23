# coding=UTF-8
from pygramadan.attributes import Gender, Strength
from pygramadan.noun import Noun
from pygramadan.wiktionary_inflection import noun_f2, noun_f3, noun_f4, noun_m1, noun_m2, noun_m3, noun_m4, noun_f5, noun_m5, noun_mV, split_tpl_params
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
import io
from pytest import raises


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


ROINN_XML = """
<noun default="roinn" declension="3" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="roinn" gender="masc" />
  <sgGen default="ranna" gender="masc" />
  <plNom default="ranna" />
  <plGen default="rann" strength="weak" />
</noun>
"""


ROINN_WIKI = "{{ga-decl-m3|r|oinn|anna|anna|ann}}"


CODLADH_XML = """
<noun default="codladh" declension="3" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="codladh" gender="masc" />
  <sgGen default="codlata" gender="masc" />
</noun>
"""


CODLADH_WIKI = "{{ga-decl-m3-nopl|c|odladh|odlata}}"


def test_noun_m3():
    sio = io.StringIO(ROINN_XML)
    roinn_xml = Noun(source=sio)
    roinn_wiki = noun_m3(ROINN_WIKI)
    assert roinn_xml.get_lemma() == roinn_wiki.get_lemma()
    assert roinn_xml.get_gender() == roinn_wiki.get_gender()
    assert len(roinn_xml.pl_gen) == len(roinn_wiki.pl_gen)
    assert roinn_xml.pl_gen[0].value == roinn_wiki.pl_gen[0].value
    assert roinn_xml.pl_gen[0].strength == roinn_wiki.pl_gen[0].strength

    sio = io.StringIO(CODLADH_XML)
    codladh_xml = Noun(source=sio)
    codladh_wiki = noun_m3(CODLADH_WIKI)
    assert codladh_xml.get_lemma() == codladh_wiki.get_lemma()
    assert codladh_xml.get_gender() == codladh_wiki.get_gender()
    assert len(codladh_xml.pl_gen) == len(codladh_wiki.pl_gen) == 0


PANDA_XML = """
<noun default="panda" declension="4" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="panda" gender="masc" />
  <sgGen default="panda" gender="masc" />
  <plNom default="pandaí" />
  <plGen default="pandaí" strength="strong" />
</noun>
"""


PANDA_WIKI = "{{ga-decl-m4|p|anda|andaí}}"


POITIN_XML = """
<noun default="poitín" declension="4" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="poitín" gender="masc" />
  <sgGen default="poitín" gender="masc" />
</noun>
"""


POITIN_WIKI = "{{ga-decl-m4-nopl|p|oitín}}"


def test_noun_m4():
    sio = io.StringIO(PANDA_XML)
    panda_xml = Noun(source=sio)
    panda_wiki = noun_m4(PANDA_WIKI)
    assert panda_xml.get_lemma() == panda_wiki.get_lemma()
    assert panda_xml.get_gender() == panda_wiki.get_gender()
    assert len(panda_xml.pl_gen) == len(panda_wiki.pl_gen)
    assert panda_xml.pl_gen[0].value == panda_wiki.pl_gen[0].value
    assert panda_xml.pl_gen[0].strength == panda_wiki.pl_gen[0].strength

    sio = io.StringIO(POITIN_XML)
    poitin_xml = Noun(source=sio)
    poitin_wiki = noun_m4(POITIN_WIKI)
    assert poitin_xml.get_lemma() == poitin_wiki.get_lemma()
    assert poitin_xml.get_gender() == poitin_wiki.get_gender()


SLAINTE_XML = """
<noun default="sláinte" declension="4" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="sláinte" gender="fem" />
  <sgGen default="sláinte" gender="fem" />
  <plNom default="sláintí" />
  <plGen default="sláintí" strength="strong" />
</noun>
"""


SLAINTE_WIKI = "{{ga-decl-f4|sl|áinte|áintí}}"


SAOIRSE_XML = """
<noun default="saoirse" declension="4" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="saoirse" gender="fem" />
  <sgGen default="saoirse" gender="fem" />
</noun>
"""


SAOIRSE_WIKI = "{{ga-decl-f4-nopl|sa|oirse}}"


def test_noun_f4():
    sio = io.StringIO(SLAINTE_XML)
    slainte_xml = Noun(source=sio)
    slainte_wiki = noun_f4(SLAINTE_WIKI)
    assert slainte_xml.get_lemma() == slainte_wiki.get_lemma()
    assert slainte_xml.get_gender() == slainte_wiki.get_gender()
    assert len(slainte_xml.pl_gen) == len(slainte_wiki.pl_gen)
    assert slainte_xml.pl_gen[0].value == slainte_wiki.pl_gen[0].value
    assert slainte_xml.pl_gen[0].strength == slainte_wiki.pl_gen[0].strength

    sio = io.StringIO(SAOIRSE_XML)
    saoirse_xml = Noun(source=sio)
    saoirse_wiki = noun_f4(SAOIRSE_WIKI)
    assert saoirse_xml.get_lemma() == saoirse_wiki.get_lemma()
    assert saoirse_xml.get_gender() == saoirse_wiki.get_gender()


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


TEACH_XML = """
<noun default="teach" declension="2" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="teach" gender="masc" />
  <sgGen default="tí" gender="masc" />
  <sgDat default="tigh" gender="masc" />
  <plNom default="tithe" />
  <plGen default="tithe" strength="strong" />
</noun>
"""


TEACH_WIKI = "{{ga-decl-m2|t|each|í|pl=ithe|dat=igh|datoc=p}}"


def test_noun_m2():
    sio = io.StringIO(TEACH_XML)
    teach_xml = Noun(source=sio)
    teach_wiki = noun_m2(TEACH_WIKI)
    assert teach_xml.get_lemma() == teach_wiki.get_lemma()
    assert teach_xml.get_gender() == teach_wiki.get_gender()
    assert len(teach_xml.pl_gen) == len(teach_wiki.pl_gen)
    assert teach_xml.pl_gen[0].value == teach_wiki.pl_gen[0].value
    assert teach_xml.pl_gen[0].value == teach_wiki.pl_gen[0].value
    assert teach_xml.pl_gen[0].strength == teach_wiki.pl_gen[0].strength
    assert teach_xml.sg_dat[0].value == teach_wiki.sg_dat[0].value


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
    caora_xml = Noun(source=sio)
    caora_wiki = noun_f5(CAORA_WIKI)
    assert caora_xml.get_lemma() == caora_wiki.get_lemma()
    assert caora_xml.get_gender() == caora_wiki.get_gender()
    assert len(caora_xml.pl_gen) == len(caora_wiki.pl_gen)
    assert caora_xml.pl_gen[0].value == caora_wiki.pl_gen[0].value
    assert caora_xml.pl_gen[0].value == caora_wiki.pl_gen[0].value
    assert caora_xml.pl_gen[0].strength == caora_wiki.pl_gen[0].strength

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


ATHAIR_XML = """
<noun default="athair" declension="5" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="athair" gender="masc" />
  <sgGen default="athar" gender="masc" />
  <plNom default="aithreacha" />
  <plGen default="aithreacha" strength="strong" />
</noun>
"""


ATHAIR_WIKI = "{{ga-decl-m5|a|thair|thar|ithreacha}}"


def test_noun_m5():
    sio = io.StringIO(ATHAIR_XML)
    athair_xml = Noun(source=sio)
    athair_wiki = noun_m5(ATHAIR_WIKI)
    assert athair_xml.get_lemma() == athair_wiki.get_lemma()
    assert athair_xml.get_gender() == athair_wiki.get_gender()
    assert len(athair_xml.pl_gen) == len(athair_wiki.pl_gen)
    assert athair_xml.pl_gen[0].value == athair_wiki.pl_gen[0].value
    assert athair_xml.pl_gen[0].value == athair_wiki.pl_gen[0].value
    assert athair_xml.pl_gen[0].strength == athair_wiki.pl_gen[0].strength


IASC_WIKI = "{{ga-decl-m-V|iasc|éisc|éisc|iasc|decl=1|wv=y}}"
EO_WIKI = "{{ga-decl-m-V|eo|iach|iaich|iach|decl=5}}"


def test_noun_mV():
    iasc_wiki = noun_mV(IASC_WIKI)
    assert iasc_wiki.get_lemma() == "iasc"
    assert iasc_wiki.get_gender() == Gender.Masc
    assert len(iasc_wiki.pl_gen) == 1
    assert iasc_wiki.pl_gen[0].value == "iasc"
    assert iasc_wiki.sg_voc[0].value == "éisc"
    assert iasc_wiki.pl_gen[0].strength == Strength.Weak
    assert iasc_wiki.pl_voc[0].value == "iasca"

    eo_wiki = noun_mV(EO_WIKI)
    assert eo_wiki.get_lemma() == "eo"
    assert eo_wiki.get_gender() == Gender.Masc
    assert len(eo_wiki.pl_gen) == 1
    assert eo_wiki.pl_gen[0].value == "iach"
    assert eo_wiki.sg_voc[0].value == "eo"
    assert eo_wiki.pl_gen[0].strength == Strength.Weak
    assert eo_wiki.pl_voc[0].value == "iaich"

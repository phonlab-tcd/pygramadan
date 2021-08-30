# coding=UTF-8
from pygramadan.noun import Noun
from pygramadan.forms import Form, FormSg, FormPlGen
from pygramadan.attributes import Gender, Strength
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
import io

AINM_XML_HEADER = """
<?xml version='1.0' encoding='utf-8'?>
<noun default="ainm" declension="4" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="ainm" gender="masc" />
  <sgGen default="ainm" gender="masc" />
  <plNom default="ainmneacha" />
  <plGen default="ainmneacha" strength="strong" />
</noun>
"""

AINM_XML = """
<noun default="ainm" declension="4" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="ainm" gender="masc" />
  <sgGen default="ainm" gender="masc" />
  <plNom default="ainmneacha" />
  <plGen default="ainmneacha" strength="strong" />
</noun>
"""

# noqa: W291
AINM_STR = """sgNom: [ainm] 
sgGen: [ainm] 
sgVoc: [] 
sgDat: [ainm] 
plNom: [ainmneacha] 
plGen: [ainmneacha] 
plVoc: [] 
"""


def test_create():
    sg_nom = [FormSg("ainm", Gender.Masc)]
    sg_gen = [FormSg("ainm", Gender.Masc)]
    pl_nom = [Form("ainmneacha")]
    pl_gen = [FormPlGen("ainmneacha", Strength.Strong)]
    ainm = Noun(definite=False,
                proper=False,
                disambig="",
                declension=4,
                article_genitive=False,
                sg_nom=sg_nom,
                sg_gen=sg_gen,
                pl_nom=pl_nom,
                pl_gen=pl_gen)
    assert ainm is not None


def make_ainm():
    sg_nom = [FormSg("ainm", Gender.Masc)]
    sg_gen = [FormSg("ainm", Gender.Masc)]
    pl_nom = [Form("ainmneacha")]
    pl_gen = [FormPlGen("ainmneacha", Strength.Strong)]
    ainm = Noun(definite=False,
                proper=False,
                disambig="",
                declension=4,
                article_genitive=False,
                sg_nom=sg_nom,
                sg_gen=sg_gen,
                pl_nom=pl_nom,
                pl_gen=pl_gen)
    return ainm


def test_get_lemma():
    ainm = make_ainm()
    assert ainm.get_lemma() == 'ainm'


def test_get_gender():
    ainm = make_ainm()
    assert ainm.get_gender() == Gender.Masc


def test_to_xml():
    ainm = make_ainm()
    xml = ainm.to_xml()
    checker = LXMLOutputChecker()
    assert checker.check_output(AINM_XML, xml, PARSE_XML) is True


def test_str():
    ainm = make_ainm()
    txt = ainm.__str__()
    assert txt == AINM_STR


def test_read_xml():
    sio = io.StringIO(AINM_XML)
    ainm = Noun(source=sio)
    assert ainm.get_lemma() == 'ainm'
    assert ainm.get_gender() == Gender.Masc
    assert len(ainm.pl_gen) == 1
    assert ainm.pl_gen[0].value == 'ainmneacha'
    assert ainm.pl_gen[0].strength == Strength.Strong


def test_get_indentifier():
    ainm = make_ainm()
    assert ainm.get_identifier() == 'ainm_masc_4'


def test_get_all_forms():
    ainm = make_ainm()
    ainm_list = ainm.get_all_forms()
    assert len(ainm_list) == 4
    exp1 = [('sg_nom', 'ainm'), ('sg_gen', 'ainm'), ('pl_nom', 'ainmneacha'), ('pl_gen', 'ainmneacha')]
    assert ainm_list == exp1
    ainm_list2 = ainm.get_all_forms(fake_dative=True)
    assert len(ainm_list2) == 5
    exp2 = list(set(exp1 + [('sg_dat', 'ainm')]))
    assert ainm_list2 == exp2

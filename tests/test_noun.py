from pygramadan.noun import *
from pygramadan.forms import Form, FormSg, FormPlGen
from pygramadan.attributes import Gender, Strength
from doctest import Example
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML

AINM_XML_HEADER = """
<?xml version='1.0' encoding='utf-8'?>
<noun default="ainm" declension="4" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0">
  <sgNom default="ainm" gender="masc" />
  <sgGen default="ainm" gender="masc" />
  <plNom default="ainmneacha" />
  <plGen default="ainmneacha" strength="strong" />
</noun>
"""

AINM_XML = """
<noun default="ainm" declension="4" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0">
  <sgNom default="ainm" gender="masc" />
  <sgGen default="ainm" gender="masc" />
  <plNom default="ainmneacha" />
  <plGen default="ainmneacha" strength="strong" />
</noun>
"""

AINM_STR = """sgNom: [ainm] 
sgGen: [ainm] 
sgVoc: [] 
sgDat: [] 
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
        pl_gen=pl_gen
    )
    assert ainm != None

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
        pl_gen=pl_gen
    )
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
    assert checker.check_output(AINM_XML, xml, PARSE_XML) == True

def test_str():
    ainm = make_ainm()
    txt = ainm.__str__()
    assert txt == AINM_STR
# coding=UTF-8
from pygramadan.adjective import Adjective
from pygramadan.forms import Form
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
import io

_HEADER = """
<?xml version='1.0' encoding='utf-8'?>
"""

BEAG_XML ="""
<adjective default="beag" declension="1" disambig="" isPre="0">
  <sgNom default="beag" />
  <sgGenMasc default="big" />
  <sgGenFem default="bige" />
  <plNom default="beaga" />
  <graded default="lú" />
  <abstractNoun default="laghad" />
</adjective>
"""

BEAG_XML_HEADER = _HEADER + BEAG_XML


def test_create():
    sg_nom = [Form("beag")]
    sg_gen_masc = [Form("big")]
    sg_gen_fem = [Form("bige")]
    pl_nom = [Form("beaga")]
    graded = [Form("lú")]
    abstract = [Form("laghad")]
    beag = Adjective(disambig="",
                     declension=1,
                     sg_nom=sg_nom,
                     sg_gen_masc=sg_gen_masc,
                     sg_gen_fem=sg_gen_fem,
                     pl_nom=pl_nom,
                     graded=graded,
                     abstract=abstract)
    assert beag is not None


def make_beag():
    sg_nom = [Form("beag")]
    sg_gen_masc = [Form("big")]
    sg_gen_fem = [Form("bige")]
    pl_nom = [Form("beaga")]
    graded = [Form("lú")]
    abstract = [Form("laghad")]
    beag = Adjective(disambig="",
                     declension=1,
                     sg_nom=sg_nom,
                     sg_gen_masc=sg_gen_masc,
                     sg_gen_fem=sg_gen_fem,
                     pl_nom=pl_nom,
                     graded=graded,
                     abstract=abstract)
    return beag


def test_get_lemma():
    beag = make_beag()
    assert beag.get_lemma() == 'beag'


def test_read_xml():
    sio = io.StringIO(BEAG_XML)
    beag = Adjective(source=sio)
    assert beag.get_lemma() == 'beag'


def test_to_xml():
    beag = make_beag()
    xml = beag.to_xml()
    checker = LXMLOutputChecker()
    assert checker.check_output(BEAG_XML, xml, PARSE_XML) is True


def test_get_indentifier():
    beag = make_beag()
    assert beag.get_identifier() == 'beag_1'    

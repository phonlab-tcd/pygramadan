# coding=UTF-8
from pygramadan.adjective import Adjective, example_xml
from pygramadan.forms import Form
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
import io


BEAG_XML = example_xml()


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
    assert beag.get_identifier() == 'beag_adj1'


def test_get_compar_pres():
    beag = make_beag()
    assert beag.get_compar_pres()[0].value == 'níos lú'


def test_get_super_pres():
    beag = make_beag()
    assert beag.get_super_pres()[0].value == 'is lú'


def test_get_compar_past():
    beag = make_beag()
    assert beag.get_compar_past()[0].value == 'ní ba lú'
    dummy1 = Adjective(graded=[Form("adha")])
    assert dummy1.get_compar_past()[0].value == "ní b'adha"
    dummy2 = Adjective(graded=[Form("fusa")])
    assert dummy2.get_compar_past()[0].value == "ní b'fhusa"


def test_get_super_past():
    beag = make_beag()
    assert beag.get_super_past()[0].value == 'ba lú'
    dummy1 = Adjective(graded=[Form("adha")])
    assert dummy1.get_super_past()[0].value == "ab adha"
    dummy2 = Adjective(graded=[Form("fusa")])
    assert dummy2.get_super_past()[0].value == "ab fhusa"


def test_get_all_forms():
    beag = make_beag()
    beag_list = beag.get_all_forms(abstract=False)
    assert len(beag_list) == 5
    exp1 = [('sg_nom', 'beag'), ('sg_gen_masc', 'big'), ('sg_gen_fem', 'bige'), ('pl_nom', 'beaga'), ('graded', 'lú')]
    beag_list.sort()
    exp1.sort()
    assert beag_list == exp1
    beag_list2 = beag.get_all_forms()
    assert len(beag_list2) == 6
    exp2 = exp1 + [('abstract', 'laghad')]
    beag_list2.sort()
    exp2.sort()
    assert beag_list2 == exp2

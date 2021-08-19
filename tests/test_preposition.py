# coding=UTF-8
from pygramadan.preposition import Preposition
from pygramadan.forms import Form
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
import io

LE_XML = """
<preposition default="le" disambig="">
  <sg1 default="liom" />
  <sg2 default="leat" />
  <sg3Masc default="leis" />
  <sg3Fem default="léi" />
  <pl1 default="linn" />
  <pl2 default="libh" />
  <pl3 default="leo" />
</preposition>
"""


def test_create():
    le = Preposition(lemma="le",
                     disambig="",
                     sg1=[Form("liom")],
                     sg2=[Form("leat")],
                     sg3_masc=[Form("leis")],
                     sg3_fem=[Form("léi")],
                     pl1=[Form("linn")],
                     pl2=[Form("libh")],
                     pl3=[Form("leo")])
    assert le is not None


def make_le():
    le = Preposition(lemma="le",
                     disambig="",
                     sg1=[Form("liom")],
                     sg2=[Form("leat")],
                     sg3_masc=[Form("leis")],
                     sg3_fem=[Form("léi")],
                     pl1=[Form("linn")],
                     pl2=[Form("libh")],
                     pl3=[Form("leo")])
    return le


def test_getlemma():
    le = make_le()
    assert le.get_lemma() == 'le'


def test_to_xml():
    le = make_le()
    xml = le.to_xml()
    checker = LXMLOutputChecker()
    assert checker.check_output(LE_XML, xml, PARSE_XML) is True


def test_read_xml():
    sio = io.StringIO(LE_XML)
    le = Preposition(source=sio)
    assert le.get_lemma() == 'le'
    assert le.sg3_masc[0].value == "leis"


def make_in_aice_le():
    in_aice_le = Preposition(lemma="in aice le",
                             disambig="")
    return in_aice_le


def test_get_identifier():
    le = make_le()
    assert le.get_identifier() == 'le_prep'
    in_aice_le = make_in_aice_le()
    assert in_aice_le.get_identifier() == 'in_aice_le_prep'


def test_is_empty():
    le = make_le()
    assert le.is_empty() is False
    in_aice_le = make_in_aice_le()
    assert in_aice_le.is_empty() is True

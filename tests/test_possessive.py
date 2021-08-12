# coding=UTF-8
from pygramadan.attributes import Mutation
from pygramadan.possessive import Possessive
from pygramadan.forms import Form
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
import io

DO_XML = """
<possessive default="do" disambig="" mutation="len1">
        <full default="do" />
        <apos default="d'" />
</possessive>
"""


def test_create():
    do = Possessive(disambig="",
                    mutation="len1",
                    full=[Form("do")],
                    apos=[Form("d'")])
    assert do is not None


def make_do():
    do = Possessive(disambig="",
                    mutation="len1",
                    full=[Form("do")],
                    apos=[Form("d'")])
    return do


def test_getlemma():
    do = make_do()
    assert do.get_lemma() == 'do'


def test_to_xml():
    do = make_do()
    xml = do.to_xml()
    checker = LXMLOutputChecker()
    assert checker.check_output(DO_XML, xml, PARSE_XML) is True


def test_read_xml():
    sio = io.StringIO(DO_XML)
    do = Possessive(source=sio)
    assert do.get_lemma() == 'do'
    assert do.mutation == Mutation.Len1
    assert do.apos[0].value == "d'"

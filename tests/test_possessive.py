# coding=UTF-8
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
    full = [Form("do")]
    apos = [Form("d'")]
    do = Possessive(disambig="",
                    mutation="len1",
                    full=full,
                    apos=apos)
    assert do is not None

from .test_noun import make_ainm
from pygramadan.printer_neid import PrinterNeid
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML


_NOUN_XML = """
<Lemma lemma="ainm" uid="ainm_masc_4">
<noun gender="masc" declension="4">
  <sgNom>
    <articleNo>ainm</articleNo>
    <articleYes>an t-ainm</articleYes>
  </sgNom>
</noun>
</Lemma>
"""


def test_print_noun():
    pn = PrinterNeid()
    out = pn.print_noun_xml(make_ainm())
    checker = LXMLOutputChecker()
    assert checker.check_output(_NOUN_XML, out, PARSE_XML) is True

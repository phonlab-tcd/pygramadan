from .test_noun import make_ainm
from .test_noun_phrase import FEAR_POIST_XML
from pygramadan.printer_neid import PrinterNeid
from pygramadan.noun_phrase import NP
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
import io


_NOUN_XML = """
<Lemma lemma="ainm" uid="ainm_masc_4">
<noun gender="masc" declension="4">
  <sgNom>
    <articleNo>ainm</articleNo>
    <articleYes>an t-ainm</articleYes>
  </sgNom>
  <sgGen>
    <articleNo>ainm</articleNo>
    <articleYes>an ainm</articleYes>
  </sgGen>
  <plNom>
    <articleNo>ainmneacha</articleNo>
    <articleYes>na hainmneacha</articleYes>
  </plNom>
  <plGen>
    <articleNo>ainmneacha</articleNo>
    <articleYes>na n-ainmneacha</articleYes>
  </plGen>
</noun>
</Lemma>
"""


_NP_XML = """
<Lemma lemma="fear poist" uid="fear_poist_NP">
<nounPhrase gender="masc" forceNominative="1">
  <sgNom>
    <articleNo>fear poist</articleNo>
    <articleYes>an fear poist</articleYes>
  </sgNom>
  <sgGen>
    <articleNo>fir phoist</articleNo>
    <articleYes>an fhir phoist</articleYes>
  </sgGen>
  <plNom>
    <articleNo>fir phoist</articleNo>
    <articleYes>na fir phoist</articleYes>
  </plNom>
  <plGen>
    <articleNo>fear poist</articleNo>
    <articleYes>na bhfear poist</articleYes>
  </plGen>
</nounPhrase>
</Lemma>
"""


def test_print_noun():
    pn = PrinterNeid(with_xml_declarations=True)
    out = pn.print_noun_xml(make_ainm())
    checker = LXMLOutputChecker()
    assert checker.check_output(_NOUN_XML, out, PARSE_XML) is True
    assert bytes('xml-stylesheet', encoding='UTF-8') in out


def test_print_noun_no_decl():
    pn = PrinterNeid(with_xml_declarations=False)
    out = pn.print_noun_xml(make_ainm())
    checker = LXMLOutputChecker()
    assert checker.check_output(_NOUN_XML, out, PARSE_XML) is True
    assert bytes('xml-stylesheet', encoding='UTF-8') not in out


def test_print_np():
    pn = PrinterNeid(with_xml_declarations=False)
    sio = io.StringIO(FEAR_POIST_XML)
    out = pn.print_np_xml(NP(source=sio))
    checker = LXMLOutputChecker()
    assert checker.check_output(_NP_XML, out, PARSE_XML) is True

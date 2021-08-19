from pygramadan.preposition import Preposition
from .test_adjective import make_beag
from .test_noun import make_ainm
from .test_noun_phrase import FEAR_POIST_XML
from .test_preposition import LE_XML
from pygramadan.printer_neid import PrinterNeid
from pygramadan.noun_phrase import NP
from pygramadan.prepositional_phrase import PP
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


_PP_XML = """
<Lemma lemma="le fear poist" uid="le_fear_poist_PP">
<prepositionalPhrase>
  <sg>
    <articleNo>le fear poist</articleNo>
    <articleYes var='north'>leis an fhear poist</articleYes>
    <articleYes var='south'>leis an bhfear poist</articleYes>
  </sg>
</prepositionalPhrase>
</Lemma>
"""


_BEAG_XML = """
<Lemma lemma="beag" uid="beag_adj1">
<adjective declension="1">
  <sgNomMasc>beag</sgNomMasc>
  <sgNomFem>bheag</sgNomFem>
  <sgGenMasc>bhig</sgGenMasc>
  <sgGenFem>bige</sgGenFem>
  <plNom>beaga</plNom>
  <plNomSlen>bheaga</plNomSlen>
  <plGenStrong>beaga</plGenStrong>
  <plGenWeak>beag</plGenWeak>
  <comparPres>níos lú</comparPres>
  <comparPast>ní ba lú</comparPast>
  <superPres>is lú</superPres>
  <superPast>ba lú</superPast>
  <abstractNoun>laghad</abstractNoun>
  <abstractNounExamples>
    <example>dá laghad</example>
    <example>ag dul i laghad</example>
  </abstractNounExamples>
</adjective>
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


def test_print_adj():
    pn = PrinterNeid(with_xml_declarations=False)
    out = pn.print_adjective(make_beag())
    checker = LXMLOutputChecker()
    assert checker.check_output(_BEAG_XML, out, PARSE_XML) is True


def test_print_pp():
    pn = PrinterNeid(with_xml_declarations=False)
    sio = io.StringIO(FEAR_POIST_XML)
    np = NP(source=sio)
    sio2 = io.StringIO(LE_XML)
    prp = Preposition(source=sio2)
    pp = PP(preposition=prp, np=np)
    out = pn.print_pp_xml(pp)
    checker = LXMLOutputChecker()
    assert checker.check_output(_PP_XML, out, PARSE_XML) is True

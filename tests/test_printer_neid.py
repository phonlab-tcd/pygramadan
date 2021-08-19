from pygramadan.preposition import Preposition
from .test_adjective import make_beag
from .test_noun import make_ainm
from .test_noun_phrase import FEAR_POIST_XML
from .test_preposition import LE_XML, make_le
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
<Lemma lemma="le hainm beag" uid="le_hainm_beag_PP">
<prepositionalPhrase>
  <sg>
    <articleNo>le hainm beag</articleNo>
    <articleYes var='north'>leis an ainm bheag</articleYes>
    <articleYes var='south'>leis an ainm beag</articleYes>
  </sg>
  <pl>
    <articleNo>le hainmneacha beaga</articleNo>
    <articleYes>leis na hainmneacha beaga</articleYes>
  </pl>
</prepositionalPhrase>
</Lemma>
"""


_PREP_XML = """
<Lemma lemma="le" uid="le_prep">
<preposition>
  <persSg1>liom</persSg1>
  <persSg2>leat</persSg2>
  <persSg3Masc>leis</persSg3Masc>
  <persSg3Fem>léi</persSg3Fem>
  <persPl1>linn</persPl1>
  <persPl2>libh</persPl2>
  <persPl3>leo</persPl3>
</preposition>
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
    out = pn.print_adjective_xml(make_beag())
    checker = LXMLOutputChecker()
    assert checker.check_output(_BEAG_XML, out, PARSE_XML) is True


def test_print_prep():
    pn = PrinterNeid(with_xml_declarations=False)
    out = pn.print_preposition_xml(make_le())
    checker = LXMLOutputChecker()
    assert checker.check_output(_PREP_XML, out, PARSE_XML) is True


def test_print_pp():
    pn = PrinterNeid(with_xml_declarations=False)
    sio = io.StringIO(FEAR_POIST_XML)
    np = NP(noun=make_ainm(), adjective=make_beag())
    sio2 = io.StringIO(LE_XML)
    prp = Preposition(source=sio2)
    pp = PP(preposition=prp, np=np)
    out = pn.print_pp_xml(pp)
    checker = LXMLOutputChecker()
    assert checker.check_output(_PP_XML, out, PARSE_XML) is True

from pygramadan.preposition import Preposition
from .test_adjective import make_beag
from .test_noun import make_ainm
from .test_noun_phrase import FEAR_POIST_XML
from .test_preposition import LE_XML, make_le
from .test_verb import AIMSIGH_XML_FULL, Verb
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
  <persSg3Fem>l??i</persSg3Fem>
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
  <comparPres>n??os l??</comparPres>
  <comparPast>n?? ba l??</comparPast>
  <superPres>is l??</superPres>
  <superPast>ba l??</superPast>
  <abstractNoun>laghad</abstractNoun>
  <abstractNounExamples>
    <example>d?? laghad</example>
    <example>ag dul i laghad</example>
  </abstractNounExamples>
</adjective>
</Lemma>
"""


_AIMSIGH_XML = """
<Lemma lemma='aimsigh' uid='aimsigh_verb'>
<verb>
	<vn>aimsi??</vn>
	<va>aimsithe</va>
	<past>
		<sg1>
			<pos>d&apos;aimsigh m??</pos>
			<quest>ar aimsigh m???</quest>
			<neg>n??or aimsigh m??</neg>
		</sg1>
		<sg2>
			<pos>d&apos;aimsigh t??</pos>
			<quest>ar aimsigh t???</quest>
			<neg>n??or aimsigh t??</neg>
		</sg2>
		<sg3Masc>
			<pos>d&apos;aimsigh s??</pos>
			<quest>ar aimsigh s???</quest>
			<neg>n??or aimsigh s??</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>d&apos;aimsigh s??</pos>
			<quest>ar aimsigh s???</quest>
			<neg>n??or aimsigh s??</neg>
		</sg3Fem>
		<pl1>
			<pos>d&apos;aims??omar</pos>
			<pos>d&apos;aimsigh muid</pos>
			<quest>ar aims??omar?</quest>
			<quest>ar aimsigh muid?</quest>
			<neg>n??or aims??omar</neg>
			<neg>n??or aimsigh muid</neg>
		</pl1>
		<pl2>
			<pos>d&apos;aimsigh sibh</pos>
			<quest>ar aimsigh sibh?</quest>
			<neg>n??or aimsigh sibh</neg>
		</pl2>
		<pl3>
			<pos>d&apos;aimsigh siad</pos>
			<pos>d&apos;aims??odar</pos>
			<quest>ar aimsigh siad?</quest>
			<quest>ar aims??odar?</quest>
			<neg>n??or aimsigh siad</neg>
			<neg>n??or aims??odar</neg>
		</pl3>
		<auto>
			<pos>aims??odh</pos>
			<quest>ar aims??odh?</quest>
			<neg>n??or aims??odh</neg>
		</auto>
	</past>
	<present>
		<sg1>
			<pos>aims??m</pos>
			<quest>an aims??m?</quest>
			<neg>n?? aims??m</neg>
		</sg1>
		<sg2>
			<pos>aims??onn t??</pos>
			<quest>an aims??onn t???</quest>
			<neg>n?? aims??onn t??</neg>
		</sg2>
		<sg3Masc>
			<pos>aims??onn s??</pos>
			<quest>an aims??onn s???</quest>
			<neg>n?? aims??onn s??</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>aims??onn s??</pos>
			<quest>an aims??onn s???</quest>
			<neg>n?? aims??onn s??</neg>
		</sg3Fem>
		<pl1>
			<pos>aims??mid</pos>
			<pos>aims??onn muid</pos>
			<quest>an aims??mid?</quest>
			<quest>an aims??onn muid?</quest>
			<neg>n?? aims??mid</neg>
			<neg>n?? aims??onn muid</neg>
		</pl1>
		<pl2>
			<pos>aims??onn sibh</pos>
			<quest>an aims??onn sibh?</quest>
			<neg>n?? aims??onn sibh</neg>
		</pl2>
		<pl3>
			<pos>aims??onn siad</pos>
			<quest>an aims??onn siad?</quest>
			<neg>n?? aims??onn siad</neg>
		</pl3>
		<auto>
			<pos>aims??tear</pos>
			<quest>an aims??tear?</quest>
			<neg>n?? aims??tear</neg>
		</auto>
	</present>
	<future>
		<sg1>
			<pos>aimseoidh m??</pos>
			<quest>an aimseoidh m???</quest>
			<neg>n?? aimseoidh m??</neg>
		</sg1>
		<sg2>
			<pos>aimseoidh t??</pos>
			<quest>an aimseoidh t???</quest>
			<neg>n?? aimseoidh t??</neg>
		</sg2>
		<sg3Masc>
			<pos>aimseoidh s??</pos>
			<quest>an aimseoidh s???</quest>
			<neg>n?? aimseoidh s??</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>aimseoidh s??</pos>
			<quest>an aimseoidh s???</quest>
			<neg>n?? aimseoidh s??</neg>
		</sg3Fem>
		<pl1>
			<pos>aimseoimid</pos>
			<pos>aimseoidh muid</pos>
			<quest>an aimseoimid?</quest>
			<quest>an aimseoidh muid?</quest>
			<neg>n?? aimseoimid</neg>
			<neg>n?? aimseoidh muid</neg>
		</pl1>
		<pl2>
			<pos>aimseoidh sibh</pos>
			<quest>an aimseoidh sibh?</quest>
			<neg>n?? aimseoidh sibh</neg>
		</pl2>
		<pl3>
			<pos>aimseoidh siad</pos>
			<quest>an aimseoidh siad?</quest>
			<neg>n?? aimseoidh siad</neg>
		</pl3>
		<auto>
			<pos>aimseofar</pos>
			<quest>an aimseofar?</quest>
			<neg>n?? aimseofar</neg>
		</auto>
	</future>
	<condi>
		<sg1>
			<pos>d&apos;aimseoinn</pos>
			<quest>an aimseoinn?</quest>
			<neg>n?? aimseoinn</neg>
		</sg1>
		<sg2>
			<pos>d&apos;aimseof??</pos>
			<quest>an aimseof???</quest>
			<neg>n?? aimseof??</neg>
		</sg2>
		<sg3Masc>
			<pos>d&apos;aimseodh s??</pos>
			<quest>an aimseodh s???</quest>
			<neg>n?? aimseodh s??</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>d&apos;aimseodh s??</pos>
			<quest>an aimseodh s???</quest>
			<neg>n?? aimseodh s??</neg>
		</sg3Fem>
		<pl1>
			<pos>d&apos;aimseoimis</pos>
			<pos>d&apos;aimseodh muid</pos>
			<quest>an aimseoimis?</quest>
			<quest>an aimseodh muid?</quest>
			<neg>n?? aimseoimis</neg>
			<neg>n?? aimseodh muid</neg>
		</pl1>
		<pl2>
			<pos>d&apos;aimseodh sibh</pos>
			<quest>an aimseodh sibh?</quest>
			<neg>n?? aimseodh sibh</neg>
		</pl2>
		<pl3>
			<pos>d&apos;aimseoid??s</pos>
			<pos>d&apos;aimseodh siad</pos>
			<quest>an aimseoid??s?</quest>
			<quest>an aimseodh siad?</quest>
			<neg>n?? aimseoid??s</neg>
			<neg>n?? aimseodh siad</neg>
		</pl3>
		<auto>
			<pos>d&apos;aimseofa??</pos>
			<quest>an aimseofa???</quest>
			<neg>n?? aimseofa??</neg>
		</auto>
	</condi>
	<pastConti>
		<sg1>
			<pos>d&apos;aims??nn</pos>
			<quest>an aims??nn?</quest>
			<neg>n?? aims??nn</neg>
		</sg1>
		<sg2>
			<pos>d&apos;aims??te??</pos>
			<quest>an aims??te???</quest>
			<neg>n?? aims??te??</neg>
		</sg2>
		<sg3Masc>
			<pos>d&apos;aims??odh s??</pos>
			<quest>an aims??odh s???</quest>
			<neg>n?? aims??odh s??</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>d&apos;aims??odh s??</pos>
			<quest>an aims??odh s???</quest>
			<neg>n?? aims??odh s??</neg>
		</sg3Fem>
		<pl1>
			<pos>d&apos;aims??mis</pos>
			<pos>d&apos;aims??odh muid</pos>
			<quest>an aims??mis?</quest>
			<quest>an aims??odh muid?</quest>
			<neg>n?? aims??mis</neg>
			<neg>n?? aims??odh muid</neg>
		</pl1>
		<pl2>
			<pos>d&apos;aims??odh sibh</pos>
			<quest>an aims??odh sibh?</quest>
			<neg>n?? aims??odh sibh</neg>
		</pl2>
		<pl3>
			<pos>d&apos;aims??d??s</pos>
			<pos>d&apos;aims??odh siad</pos>
			<quest>an aims??d??s?</quest>
			<quest>an aims??odh siad?</quest>
			<neg>n?? aims??d??s</neg>
			<neg>n?? aims??odh siad</neg>
		</pl3>
		<auto>
			<pos>d&apos;aims??t??</pos>
			<quest>an aims??t???</quest>
			<neg>n?? aims??t??</neg>
		</auto>
	</pastConti>
	<imper>
		<sg1>
			<pos>aims??m!</pos>
			<neg>n?? haims??m!</neg>
		</sg1>
		<sg2>
			<pos>aimsigh!</pos>
			<neg>n?? haimsigh!</neg>
		</sg2>
		<sg3Masc>
			<pos>aims??odh s??!</pos>
			<neg>n?? haims??odh s??!</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>aims??odh s??!</pos>
			<neg>n?? haims??odh s??!</neg>
		</sg3Fem>
		<pl1>
			<pos>aims??mis!</pos>
			<pos>aims??odh muid!</pos>
			<neg>n?? haims??mis!</neg>
			<neg>n?? haims??odh muid!</neg>
		</pl1>
		<pl2>
			<pos>aims??g??!</pos>
			<neg>n?? haims??g??!</neg>
		</pl2>
		<pl3>
			<pos>aims??d??s!</pos>
			<pos>aims??odh siad!</pos>
			<neg>n?? haims??d??s!</neg>
			<neg>n?? haims??odh siad!</neg>
		</pl3>
		<auto>
			<pos>aims??tear!</pos>
			<neg>n?? haims??tear!</neg>
		</auto>
	</imper>
	<subj>
		<sg1>
			<pos>go n-aims?? m??</pos>
			<neg>n??r aims?? m??</neg>
		</sg1>
		<sg2>
			<pos>go n-aims?? t??</pos>
			<neg>n??r aims?? t??</neg>
		</sg2>
		<sg3Masc>
			<pos>go n-aims?? s??</pos>
			<neg>n??r aims?? s??</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>go n-aims?? s??</pos>
			<neg>n??r aims?? s??</neg>
		</sg3Fem>
		<pl1>
			<pos>go n-aims??mid</pos>
			<pos>go n-aims?? muid</pos>
			<neg>n??r aims??mid</neg>
			<neg>n??r aims?? muid</neg>
		</pl1>
		<pl2>
			<pos>go n-aims?? sibh</pos>
			<neg>n??r aims?? sibh</neg>
		</pl2>
		<pl3>
			<pos>go n-aims?? siad</pos>
			<neg>n??r aims?? siad</neg>
		</pl3>
		<auto>
			<pos>go n-aims??tear</pos>
			<neg>n??r aims??tear</neg>
		</auto>
	</subj>
</verb>
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
    np = NP(noun=make_ainm(), adjective=make_beag())
    sio = io.StringIO(LE_XML)
    prp = Preposition(source=sio)
    pp = PP(preposition=prp, np=np)
    out = pn.print_pp_xml(pp)
    checker = LXMLOutputChecker()
    assert checker.check_output(_PP_XML, out, PARSE_XML) is True


def test_print_verb():
    pn = PrinterNeid(with_xml_declarations=False)
    sio = io.StringIO(AIMSIGH_XML_FULL)
    v = Verb(source=sio)
    out = pn.print_verb_xml(v)
    checker = LXMLOutputChecker()
    assert checker.check_output(_AIMSIGH_XML, out, PARSE_XML) is True

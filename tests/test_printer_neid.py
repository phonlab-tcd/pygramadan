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


_AIMSIGH_XML = """
<Lemma lemma='aimsigh' uid='aimsigh_verb'>
<verb>
	<vn>aimsiú</vn>
	<va>aimsithe</va>
	<past>
		<sg1>
			<pos>d&apos;aimsigh mé</pos>
			<quest>ar aimsigh mé?</quest>
			<neg>níor aimsigh mé</neg>
		</sg1>
		<sg2>
			<pos>d&apos;aimsigh tú</pos>
			<quest>ar aimsigh tú?</quest>
			<neg>níor aimsigh tú</neg>
		</sg2>
		<sg3Masc>
			<pos>d&apos;aimsigh sé</pos>
			<quest>ar aimsigh sé?</quest>
			<neg>níor aimsigh sé</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>d&apos;aimsigh sí</pos>
			<quest>ar aimsigh sí?</quest>
			<neg>níor aimsigh sí</neg>
		</sg3Fem>
		<pl1>
			<pos>d&apos;aimsíomar</pos>
			<pos>d&apos;aimsigh muid</pos>
			<quest>ar aimsíomar?</quest>
			<quest>ar aimsigh muid?</quest>
			<neg>níor aimsíomar</neg>
			<neg>níor aimsigh muid</neg>
		</pl1>
		<pl2>
			<pos>d&apos;aimsigh sibh</pos>
			<quest>ar aimsigh sibh?</quest>
			<neg>níor aimsigh sibh</neg>
		</pl2>
		<pl3>
			<pos>d&apos;aimsigh siad</pos>
			<pos>d&apos;aimsíodar</pos>
			<quest>ar aimsigh siad?</quest>
			<quest>ar aimsíodar?</quest>
			<neg>níor aimsigh siad</neg>
			<neg>níor aimsíodar</neg>
		</pl3>
		<auto>
			<pos>aimsíodh</pos>
			<quest>ar aimsíodh?</quest>
			<neg>níor aimsíodh</neg>
		</auto>
	</past>
	<present>
		<sg1>
			<pos>aimsím</pos>
			<quest>an aimsím?</quest>
			<neg>ní aimsím</neg>
		</sg1>
		<sg2>
			<pos>aimsíonn tú</pos>
			<quest>an aimsíonn tú?</quest>
			<neg>ní aimsíonn tú</neg>
		</sg2>
		<sg3Masc>
			<pos>aimsíonn sé</pos>
			<quest>an aimsíonn sé?</quest>
			<neg>ní aimsíonn sé</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>aimsíonn sí</pos>
			<quest>an aimsíonn sí?</quest>
			<neg>ní aimsíonn sí</neg>
		</sg3Fem>
		<pl1>
			<pos>aimsímid</pos>
			<pos>aimsíonn muid</pos>
			<quest>an aimsímid?</quest>
			<quest>an aimsíonn muid?</quest>
			<neg>ní aimsímid</neg>
			<neg>ní aimsíonn muid</neg>
		</pl1>
		<pl2>
			<pos>aimsíonn sibh</pos>
			<quest>an aimsíonn sibh?</quest>
			<neg>ní aimsíonn sibh</neg>
		</pl2>
		<pl3>
			<pos>aimsíonn siad</pos>
			<quest>an aimsíonn siad?</quest>
			<neg>ní aimsíonn siad</neg>
		</pl3>
		<auto>
			<pos>aimsítear</pos>
			<quest>an aimsítear?</quest>
			<neg>ní aimsítear</neg>
		</auto>
	</present>
	<future>
		<sg1>
			<pos>aimseoidh mé</pos>
			<quest>an aimseoidh mé?</quest>
			<neg>ní aimseoidh mé</neg>
		</sg1>
		<sg2>
			<pos>aimseoidh tú</pos>
			<quest>an aimseoidh tú?</quest>
			<neg>ní aimseoidh tú</neg>
		</sg2>
		<sg3Masc>
			<pos>aimseoidh sé</pos>
			<quest>an aimseoidh sé?</quest>
			<neg>ní aimseoidh sé</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>aimseoidh sí</pos>
			<quest>an aimseoidh sí?</quest>
			<neg>ní aimseoidh sí</neg>
		</sg3Fem>
		<pl1>
			<pos>aimseoimid</pos>
			<pos>aimseoidh muid</pos>
			<quest>an aimseoimid?</quest>
			<quest>an aimseoidh muid?</quest>
			<neg>ní aimseoimid</neg>
			<neg>ní aimseoidh muid</neg>
		</pl1>
		<pl2>
			<pos>aimseoidh sibh</pos>
			<quest>an aimseoidh sibh?</quest>
			<neg>ní aimseoidh sibh</neg>
		</pl2>
		<pl3>
			<pos>aimseoidh siad</pos>
			<quest>an aimseoidh siad?</quest>
			<neg>ní aimseoidh siad</neg>
		</pl3>
		<auto>
			<pos>aimseofar</pos>
			<quest>an aimseofar?</quest>
			<neg>ní aimseofar</neg>
		</auto>
	</future>
	<condi>
		<sg1>
			<pos>d&apos;aimseoinn</pos>
			<quest>an aimseoinn?</quest>
			<neg>ní aimseoinn</neg>
		</sg1>
		<sg2>
			<pos>d&apos;aimseofá</pos>
			<quest>an aimseofá?</quest>
			<neg>ní aimseofá</neg>
		</sg2>
		<sg3Masc>
			<pos>d&apos;aimseodh sé</pos>
			<quest>an aimseodh sé?</quest>
			<neg>ní aimseodh sé</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>d&apos;aimseodh sí</pos>
			<quest>an aimseodh sí?</quest>
			<neg>ní aimseodh sí</neg>
		</sg3Fem>
		<pl1>
			<pos>d&apos;aimseoimis</pos>
			<pos>d&apos;aimseodh muid</pos>
			<quest>an aimseoimis?</quest>
			<quest>an aimseodh muid?</quest>
			<neg>ní aimseoimis</neg>
			<neg>ní aimseodh muid</neg>
		</pl1>
		<pl2>
			<pos>d&apos;aimseodh sibh</pos>
			<quest>an aimseodh sibh?</quest>
			<neg>ní aimseodh sibh</neg>
		</pl2>
		<pl3>
			<pos>d&apos;aimseoidís</pos>
			<pos>d&apos;aimseodh siad</pos>
			<quest>an aimseoidís?</quest>
			<quest>an aimseodh siad?</quest>
			<neg>ní aimseoidís</neg>
			<neg>ní aimseodh siad</neg>
		</pl3>
		<auto>
			<pos>d&apos;aimseofaí</pos>
			<quest>an aimseofaí?</quest>
			<neg>ní aimseofaí</neg>
		</auto>
	</condi>
	<pastConti>
		<sg1>
			<pos>d&apos;aimsínn</pos>
			<quest>an aimsínn?</quest>
			<neg>ní aimsínn</neg>
		</sg1>
		<sg2>
			<pos>d&apos;aimsíteá</pos>
			<quest>an aimsíteá?</quest>
			<neg>ní aimsíteá</neg>
		</sg2>
		<sg3Masc>
			<pos>d&apos;aimsíodh sé</pos>
			<quest>an aimsíodh sé?</quest>
			<neg>ní aimsíodh sé</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>d&apos;aimsíodh sí</pos>
			<quest>an aimsíodh sí?</quest>
			<neg>ní aimsíodh sí</neg>
		</sg3Fem>
		<pl1>
			<pos>d&apos;aimsímis</pos>
			<pos>d&apos;aimsíodh muid</pos>
			<quest>an aimsímis?</quest>
			<quest>an aimsíodh muid?</quest>
			<neg>ní aimsímis</neg>
			<neg>ní aimsíodh muid</neg>
		</pl1>
		<pl2>
			<pos>d&apos;aimsíodh sibh</pos>
			<quest>an aimsíodh sibh?</quest>
			<neg>ní aimsíodh sibh</neg>
		</pl2>
		<pl3>
			<pos>d&apos;aimsídís</pos>
			<pos>d&apos;aimsíodh siad</pos>
			<quest>an aimsídís?</quest>
			<quest>an aimsíodh siad?</quest>
			<neg>ní aimsídís</neg>
			<neg>ní aimsíodh siad</neg>
		</pl3>
		<auto>
			<pos>d&apos;aimsítí</pos>
			<quest>an aimsítí?</quest>
			<neg>ní aimsítí</neg>
		</auto>
	</pastConti>
	<imper>
		<sg1>
			<pos>aimsím!</pos>
			<neg>ná haimsím!</neg>
		</sg1>
		<sg2>
			<pos>aimsigh!</pos>
			<neg>ná haimsigh!</neg>
		</sg2>
		<sg3Masc>
			<pos>aimsíodh sé!</pos>
			<neg>ná haimsíodh sé!</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>aimsíodh sí!</pos>
			<neg>ná haimsíodh sí!</neg>
		</sg3Fem>
		<pl1>
			<pos>aimsímis!</pos>
			<pos>aimsíodh muid!</pos>
			<neg>ná haimsímis!</neg>
			<neg>ná haimsíodh muid!</neg>
		</pl1>
		<pl2>
			<pos>aimsígí!</pos>
			<neg>ná haimsígí!</neg>
		</pl2>
		<pl3>
			<pos>aimsídís!</pos>
			<pos>aimsíodh siad!</pos>
			<neg>ná haimsídís!</neg>
			<neg>ná haimsíodh siad!</neg>
		</pl3>
		<auto>
			<pos>aimsítear!</pos>
			<neg>ná haimsítear!</neg>
		</auto>
	</imper>
	<subj>
		<sg1>
			<pos>go n-aimsí mé</pos>
			<neg>nár aimsí mé</neg>
		</sg1>
		<sg2>
			<pos>go n-aimsí tú</pos>
			<neg>nár aimsí tú</neg>
		</sg2>
		<sg3Masc>
			<pos>go n-aimsí sé</pos>
			<neg>nár aimsí sé</neg>
		</sg3Masc>
		<sg3Fem>
			<pos>go n-aimsí sí</pos>
			<neg>nár aimsí sí</neg>
		</sg3Fem>
		<pl1>
			<pos>go n-aimsímid</pos>
			<pos>go n-aimsí muid</pos>
			<neg>nár aimsímid</neg>
			<neg>nár aimsí muid</neg>
		</pl1>
		<pl2>
			<pos>go n-aimsí sibh</pos>
			<neg>nár aimsí sibh</neg>
		</pl2>
		<pl3>
			<pos>go n-aimsí siad</pos>
			<neg>nár aimsí siad</neg>
		</pl3>
		<auto>
			<pos>go n-aimsítear</pos>
			<neg>nár aimsítear</neg>
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
    f = open('thing.xml','w', encoding='UTF-8')
    print(out, file=f)
    checker = LXMLOutputChecker()
    assert checker.check_output(_AIMSIGH_XML, out, PARSE_XML) is True

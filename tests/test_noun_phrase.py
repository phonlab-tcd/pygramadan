from .test_adjective import make_beag
from .test_noun import make_ainm
from pygramadan.noun_phrase import NP
from pygramadan.forms import Form, FormSg, FormPlGen
from pygramadan.attributes import Gender, Strength
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
import io

FEAR_POIST_XML = """
<nounPhrase default="fear poist" disambig="" isDefinite="0" forceNominative="1">
  <sgNom default="fear poist" gender="masc" />
  <sgGen default="fir phoist" gender="masc" />
  <sgNomArt default="an fear poist" gender="masc" />
  <sgGenArt default="an fhir phoist" gender="masc" />
  <plNom default="fir phoist" />
  <plGen default="fear poist" />
  <plNomArt default="na fir phoist" />
  <plGenArt default="na bhfear poist" />
</nounPhrase>
"""


def test_read_xml():
    sio = io.StringIO(FEAR_POIST_XML)
    fear_poist = NP(source=sio)
    assert fear_poist.get_lemma() == 'fear poist'
    assert fear_poist.get_gender() == Gender.Masc
    assert fear_poist.pl_gen_art[0].value == 'na bhfear poist'


def test_noun_adj():
    beag = make_beag()
    ainm_beag = NP(noun=make_ainm(), adjective=beag)
    assert len(ainm_beag.sg_nom) == 1
    assert ainm_beag.sg_gen_art[0].value == 'an ainm bhig'
    assert ainm_beag.get_lemma() == 'ainm beag'

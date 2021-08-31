from .test_adjective import make_beag
from .test_noun import make_ainm
from pygramadan.noun_phrase import NP, example_xml
from pygramadan.attributes import Gender
import io


FEAR_POIST_XML = example_xml()


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

# coding=UTF-8
from pygramadan.attributes import VPPolarity, VPShape, VPTense
from pygramadan.verb import Verb
from pygramadan.verb_phrase import VP
from .test_verb import AIMSIGH_XML_FULL
import io

_sio = io.StringIO(AIMSIGH_XML_FULL)
_aimsigh = Verb(source=_sio)

def test_init():
    aimsigh_vp = VP(_aimsigh)
    assert aimsigh_vp is not None

_PAST_DEC_NEG = """Sg1: [níor aimsigh mé] 
Sg2: [níor aimsigh tú] 
Sg3Masc: [níor aimsigh sé] 
Sg3Fem: [níor aimsigh sí] 
Pl1: [níor aimsíomar] [níor aimsigh muid] 
Pl2: [níor aimsigh sibh] 
Pl3: [níor aimsigh siad] [níor aimsíodar] 
NoSubject: [níor aimsigh] 
Auto: [níor aimsíodh] 
"""

def test_print_tenses():
    aimsigh_vp = VP(_aimsigh)
    printed = aimsigh_vp.print_tense(VPTense.Past, VPShape.Declar, VPPolarity.Neg)
    assert printed == _PAST_DEC_NEG
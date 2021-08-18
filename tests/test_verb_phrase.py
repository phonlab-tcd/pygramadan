# coding=UTF-8
from pygramadan.verb import Verb
from pygramadan.verb_phrase import VP
from .test_verb import AIMSIGH_XML_FULL
import io


def test_init():
    sio = io.StringIO(AIMSIGH_XML_FULL)
    aimsigh = Verb(source=sio)
    aimsigh_vp = VP(aimsigh)

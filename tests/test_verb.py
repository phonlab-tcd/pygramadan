# coding=UTF-8
from pygramadan.attributes import VerbDependency, VerbMood, VerbPerson, VerbTense
from pygramadan.verb import Verb
from pygramadan.forms import Form
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
import io

_AIMSIGH_XML_FULL = """
<verb default="aimsigh" disambig="">
  <verbalNoun default="aimsiú" />
  <verbalAdjective default="aimsithe" />
  <tenseForm default="aimsigh" tense="Past" dependency="Indep" person="Base" />
  <tenseForm default="aimsíomar" tense="Past" dependency="Indep" person="Pl1" />
  <tenseForm default="aimsíodar" tense="Past" dependency="Indep" person="Pl3" />
  <tenseForm default="aimsíodh" tense="Past" dependency="Indep" person="Auto" />
  <tenseForm default="aimsigh" tense="Past" dependency="Dep" person="Base" />
  <tenseForm default="aimsíomar" tense="Past" dependency="Dep" person="Pl1" />
  <tenseForm default="aimsíodar" tense="Past" dependency="Dep" person="Pl3" />
  <tenseForm default="aimsíodh" tense="Past" dependency="Dep" person="Auto" />
  <tenseForm default="aimsíodh" tense="PastCont" dependency="Indep" person="Base" />
  <tenseForm default="aimsínn" tense="PastCont" dependency="Indep" person="Sg1" />
  <tenseForm default="aimsíteá" tense="PastCont" dependency="Indep" person="Sg2" />
  <tenseForm default="aimsímis" tense="PastCont" dependency="Indep" person="Pl1" />
  <tenseForm default="aimsídís" tense="PastCont" dependency="Indep" person="Pl3" />
  <tenseForm default="aimsítí" tense="PastCont" dependency="Indep" person="Auto" />
  <tenseForm default="aimsíodh" tense="PastCont" dependency="Dep" person="Base" />
  <tenseForm default="aimsínn" tense="PastCont" dependency="Dep" person="Sg1" />
  <tenseForm default="aimsíteá" tense="PastCont" dependency="Dep" person="Sg2" />
  <tenseForm default="aimsímis" tense="PastCont" dependency="Dep" person="Pl1" />
  <tenseForm default="aimsídís" tense="PastCont" dependency="Dep" person="Pl3" />
  <tenseForm default="aimsítí" tense="PastCont" dependency="Dep" person="Auto" />
  <tenseForm default="aimsíonn" tense="PresCont" dependency="Indep" person="Base" />
  <tenseForm default="aimsím" tense="PresCont" dependency="Indep" person="Sg1" />
  <tenseForm default="aimsímid" tense="PresCont" dependency="Indep" person="Pl1" />
  <tenseForm default="aimsítear" tense="PresCont" dependency="Indep" person="Auto" />
  <tenseForm default="aimsíonn" tense="PresCont" dependency="Dep" person="Base" />
  <tenseForm default="aimsím" tense="PresCont" dependency="Dep" person="Sg1" />
  <tenseForm default="aimsímid" tense="PresCont" dependency="Dep" person="Pl1" />
  <tenseForm default="aimsítear" tense="PresCont" dependency="Dep" person="Auto" />
  <tenseForm default="aimseoidh" tense="Fut" dependency="Indep" person="Base" />
  <tenseForm default="aimseoimid" tense="Fut" dependency="Indep" person="Pl1" />
  <tenseForm default="aimseofar" tense="Fut" dependency="Indep" person="Auto" />
  <tenseForm default="aimseoidh" tense="Fut" dependency="Dep" person="Base" />
  <tenseForm default="aimseoimid" tense="Fut" dependency="Dep" person="Pl1" />
  <tenseForm default="aimseofar" tense="Fut" dependency="Dep" person="Auto" />
  <tenseForm default="aimseodh" tense="Cond" dependency="Indep" person="Base" />
  <tenseForm default="aimseoinn" tense="Cond" dependency="Indep" person="Sg1" />
  <tenseForm default="aimseofá" tense="Cond" dependency="Indep" person="Sg2" />
  <tenseForm default="aimseoimis" tense="Cond" dependency="Indep" person="Pl1" />
  <tenseForm default="aimseoidís" tense="Cond" dependency="Indep" person="Pl3" />
  <tenseForm default="aimseofaí" tense="Cond" dependency="Indep" person="Auto" />
  <tenseForm default="aimseodh" tense="Cond" dependency="Dep" person="Base" />
  <tenseForm default="aimseoinn" tense="Cond" dependency="Dep" person="Sg1" />
  <tenseForm default="aimseofá" tense="Cond" dependency="Dep" person="Sg2" />
  <tenseForm default="aimseoimis" tense="Cond" dependency="Dep" person="Pl1" />
  <tenseForm default="aimseoidís" tense="Cond" dependency="Dep" person="Pl3" />
  <tenseForm default="aimseofaí" tense="Cond" dependency="Dep" person="Auto" />
  <moodForm default="aimsíodh" mood="Imper" person="Base" />
  <moodForm default="aimsím" mood="Imper" person="Sg1" />
  <moodForm default="aimsigh" mood="Imper" person="Sg2" />
  <moodForm default="aimsímis" mood="Imper" person="Pl1" />
  <moodForm default="aimsígí" mood="Imper" person="Pl2" />
  <moodForm default="aimsídís" mood="Imper" person="Pl3" />
  <moodForm default="aimsítear" mood="Imper" person="Auto" />
  <moodForm default="aimsí" mood="Subj" person="Base" />
  <moodForm default="aimsímid" mood="Subj" person="Pl1" />
  <moodForm default="aimsítear" mood="Subj" person="Auto" />
</verb>
"""

_AIMSIGH_XML_BASIC = """
<verb default="aimsigh" disambig="">
  <verbalNoun default="aimsiú" />
  <verbalAdjective default="aimsithe" />
  <tenseForm default="aimsigh" tense="Past" dependency="Indep" person="Base" />
  <tenseForm default="aimsíomar" tense="Past" dependency="Indep" person="Pl1" />
  <tenseForm default="aimsíodar" tense="Past" dependency="Indep" person="Pl3" />
  <moodForm default="aimsíodh" mood="Imper" person="Base" />
  <moodForm default="aimsím" mood="Imper" person="Sg1" />
  <moodForm default="aimsigh" mood="Imper" person="Sg2" />
</verb>
"""


def test_read_xml():
    sio = io.StringIO(_AIMSIGH_XML_BASIC)
    aimsigh = Verb(source=sio)
    assert aimsigh.get_lemma() == 'aimsigh'


def make_aimsigh_basic():
    tenses = {}
    for t in VerbTense:
        tenses[t] = {}
        for d in VerbDependency:
            tenses[t][d] = {}
            for p in VerbPerson:
                tenses[t][d][p] = []
    tenses[VerbTense.Past][VerbDependency.Indep][VerbPerson.Base].append(Form('aimsigh'))
    tenses[VerbTense.Past][VerbDependency.Indep][VerbPerson.Pl1].append(Form('aimsíomar'))
    tenses[VerbTense.Past][VerbDependency.Indep][VerbPerson.Pl3].append(Form('aimsíodar'))
    moods = {}
    for m in VerbMood:
        moods[m] = {}
        for p in VerbPerson:
            moods[m][p] = []
    moods[VerbMood.Imper][VerbPerson.Base].append(Form('aimsíodh'))
    moods[VerbMood.Imper][VerbPerson.Sg1].append(Form('aimsím'))
    moods[VerbMood.Imper][VerbPerson.Sg2].append(Form('aimsigh'))
    return Verb(verbal_noun=[Form('aimsiú')],
                verbal_adj=[Form('aimsithe')],
                tenses=tenses,
                moods=moods)


def test_to_xml():
    aimsigh = make_aimsigh_basic()
    xml = aimsigh.to_xml()
    checker = LXMLOutputChecker()
    assert checker.check_output(_AIMSIGH_XML_BASIC, xml, PARSE_XML) is True

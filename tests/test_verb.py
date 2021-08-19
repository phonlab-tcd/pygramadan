# coding=UTF-8
from pygramadan.attributes import Mutation, VPPerson, VPPolarity, VPShape
from pygramadan.attributes import VPTense, VerbDependency, VerbMood
from pygramadan.attributes import VerbPerson, VerbTense
from pygramadan.verb import init_moods, init_tenses, Verb
from pygramadan.forms import Form
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
import io


AIMSIGH_XML_FULL = """
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


AIMSIGH_XML_BASIC = """
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
    sio = io.StringIO(AIMSIGH_XML_BASIC)
    aimsigh = Verb(source=sio)
    assert aimsigh.moods[VerbMood.Imper][VerbPerson.Sg2][0].value == 'aimsigh'
    assert aimsigh.get_lemma() == 'aimsigh'


def make_aimsigh_basic():
    tenses = init_tenses()
    tenses[VerbTense.Past][VerbDependency.Indep][VerbPerson.Base].append(Form('aimsigh'))
    tenses[VerbTense.Past][VerbDependency.Indep][VerbPerson.Pl1].append(Form('aimsíomar'))
    tenses[VerbTense.Past][VerbDependency.Indep][VerbPerson.Pl3].append(Form('aimsíodar'))
    moods = init_moods()
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
    assert checker.check_output(AIMSIGH_XML_BASIC, xml, PARSE_XML) is True


def test_get_identifier():
    aimsigh = make_aimsigh_basic()
    assert aimsigh.get_identifier() == 'aimsigh_verb'


def test_default_tense_rule():
    aimsigh = make_aimsigh_basic()
    rules = aimsigh.get_tense_rules(VPTense.Past, VPPerson.Sg1, VPShape.Interrog, VPPolarity.Pos)
    assert len(rules) == 1
    assert rules[0].particle == 'ar'
    assert rules[0].mutation == Mutation.Len1


_ABAIR_XML_FRAG = """
<verb default="abair" disambig="">
  <verbalNoun default="rá" />
  <verbalAdjective default="ráite" />
  <tenseForm default="dúramar" tense="Past" dependency="Indep" person="Pl1" />
  <moodForm default="abair" mood="Imper" person="Sg2" />
</verb>
"""


def test_default_rule_changes():
    sio = io.StringIO(_ABAIR_XML_FRAG)
    abair = Verb(source=sio)
    rules = abair.get_tense_rules(VPTense.Past, VPPerson.Sg1, VPShape.Interrog, VPPolarity.Pos)
    # it's a silly thing, but the matching is based on lemma, so if this fails, so does the rest
    assert abair.get_lemma() == 'abair'
    assert len(rules) == 1
    # 'ar'/Len1 by default: see test_default_tense_rule()
    assert rules[0].particle == 'an'
    assert rules[0].mutation == Mutation.Ecl1x

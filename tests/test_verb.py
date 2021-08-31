# coding=UTF-8
from pygramadan.attributes import Mutation, VPPerson, VPPolarity, VPShape
from pygramadan.attributes import VPTense, VerbDependency, VerbMood
from pygramadan.attributes import VerbPerson, VerbTense
from pygramadan.verb import init_moods, init_tenses, Verb, get_example
from pygramadan.forms import Form
from lxml.doctestcompare import LXMLOutputChecker, PARSE_XML
import io


AIMSIGH_XML_FULL = get_example()


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


def test_get_all_forms():
    exp = [('cond_indep_auto', 'aimseofaí'), ('prescont_indep_sg1', 'aimsím'),
           ('pastcont_dep_sg2', 'aimsíteá'), ('fut_indep_pl1', 'aimseoimid'),
           ('prescont_dep_base', 'aimsíonn'), ('cond_dep_pl3', 'aimseoidís'),
           ('imper_pl2', 'aimsígí'), ('verbal_adj', 'aimsithe'),
           ('pastcont_dep_pl1', 'aimsímis'), ('pastcont_indep_auto', 'aimsítí'),
           ('verbal_noun', 'aimsiú'), ('past_indep_base', 'aimsigh'),
           ('past_dep_pl3', 'aimsíodar'), ('pastcont_indep_pl3', 'aimsídís'),
           ('past_indep_auto', 'aimsíodh'), ('fut_dep_pl1', 'aimseoimid'),
           ('cond_indep_pl3', 'aimseoidís'), ('fut_dep_auto', 'aimseofar'),
           ('prescont_indep_base', 'aimsíonn'), ('fut_indep_base', 'aimseoidh'),
           ('cond_indep_sg1', 'aimseoinn'), ('cond_dep_sg2', 'aimseofá'),
           ('imper_pl3', 'aimsídís'), ('subj_auto', 'aimsítear'),
           ('pastcont_indep_base', 'aimsíodh'), ('past_dep_auto', 'aimsíodh'),
           ('prescont_indep_auto', 'aimsítear'), ('prescont_indep_pl1', 'aimsímid'),
           ('pastcont_indep_pl1', 'aimsímis'), ('subj_pl1', 'aimsímid'),
           ('past_dep_base', 'aimsigh'), ('cond_dep_base', 'aimseodh'),
           ('past_dep_pl1', 'aimsíomar'), ('pastcont_dep_sg1', 'aimsínn'),
           ('subj_base', 'aimsí'), ('prescont_dep_sg1', 'aimsím'),
           ('cond_indep_base', 'aimseodh'), ('cond_dep_sg1', 'aimseoinn'),
           ('imper_sg1', 'aimsím'), ('imper_auto', 'aimsítear'),
           ('pastcont_indep_sg1', 'aimsínn'), ('cond_indep_sg2', 'aimseofá'),
           ('pastcont_indep_sg2', 'aimsíteá'), ('past_indep_pl3', 'aimsíodar'),
           ('fut_indep_auto', 'aimseofar'), ('fut_dep_base', 'aimseoidh'),
           ('pastcont_dep_base', 'aimsíodh'), ('past_indep_pl1', 'aimsíomar'),
           ('imper_pl1', 'aimsímis'), ('pastcont_dep_pl3', 'aimsídís'),
           ('cond_dep_pl1', 'aimseoimis'), ('cond_indep_pl1', 'aimseoimis'),
           ('imper_base', 'aimsíodh'), ('imper_sg2', 'aimsigh'),
           ('prescont_dep_pl1', 'aimsímid'), ('cond_dep_auto', 'aimseofaí'),
           ('pastcont_dep_auto', 'aimsítí'), ('prescont_dep_auto', 'aimsítear')]
    sio = io.StringIO(AIMSIGH_XML_FULL)
    aimsigh = Verb(source=sio)
    aimsigh_list = aimsigh.get_all_forms()
    aimsigh_list.sort()
    exp.sort()
    assert aimsigh_list == exp

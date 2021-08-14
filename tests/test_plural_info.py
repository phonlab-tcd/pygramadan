

from pygramadan.forms import Form
from pygramadan.attributes import Strength
from pygramadan.plural_info import PluralInfo, PluralInfoLgA, PluralInfoLgC, PluralInfoLgE


def test_plural_info():
    si = PluralInfo(Strength.Weak,
                    nominative=[Form("bacaigh")],
                    genitive=[Form("bacach")],
                    vocative=[Form("bacacha")])
    assert si.nominative[0].value == 'bacaigh'
    to_s = "NOM: [bacaigh] \nGEN: [bacach] \nVOC: [bacacha] \n"
    assert si.__str__() == to_s


def test_plural_info_lgc():
    si = PluralInfoLgC("bacach")
    assert si.nominative[0].value == 'bacaigh'
    assert si.genitive[0].value == 'bacach'
    assert si.vocative[0].value == 'bacacha'
    assert si.strength == Strength.Weak


def test_plural_info_lge():
    si = PluralInfoLgE("ainimh")
    assert si.nominative[0].value == 'ainimhe'
    assert si.genitive[0].value == 'aineamh'
    assert si.vocative[0].value == 'ainimhe'
    assert si.strength == Strength.Weak


def test_plural_info_lga():
    si = PluralInfoLgA("deoir")
    assert si.nominative[0].value == 'deora'
    assert si.genitive[0].value == 'deor'
    assert si.vocative[0].value == 'deora'
    assert si.strength == Strength.Weak

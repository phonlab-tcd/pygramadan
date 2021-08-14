

from pygramadan.forms import Form
from pygramadan.attributes import Strength
from pygramadan.plural_info import PluralInfo, PluralInfoLgC


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
    assert si.vocative[0].value == 'bacacha'
    assert si.strength == Strength.Weak



from pygramadan.forms import Form
from pygramadan.attributes import Strength
from pygramadan.plural_info import PluralInfo


def test_plural_info():
    si = PluralInfo(Strength.Weak,
                    nominative=[Form("bacaigh")],
                    genitive=[Form("bacach")],
                    vocative=[Form("bacacha")])
    assert si.nominative[0].value == 'bacaigh'
    to_s = "NOM: [bacaigh] \nGEN: [bacach] \nVOC: [bacacha] \n"
    assert si.__str__() == to_s

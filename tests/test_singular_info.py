from pygramadan.singular_info import *


def test_singular_info():
    si = SingularInfo(Gender.Fem,
                      nominative=[Form("bean")],
                      genitive=[Form("mná")],
                      vocative=[Form("bean")],
                      dative=[Form("mnaoi")])
    assert si.nominative[0].value == 'bean'
    to_s = "NOM: [bean] \nGEN: [mná] \nVOC: [bean] \nDAT: [mnaoi] \n"
    assert si.__str__() == to_s


def test_singular_info_o():
    si = SingularInfoO("test", Gender.Masc)
    to_s = "NOM: [test] \nGEN: [test] \nVOC: [test] \nDAT: [test] \n"
    assert si.__str__() == to_s


# This is where things start to happen
def test_singular_info_c():
    si = SingularInfoC("marcach", Gender.Masc)
    assert si.genitive[0].value == 'marcaigh'
    assert si.vocative[0].value == 'marcaigh'
    assert si.nominative[0].value == 'marcach'
    assert si.dative[0].value == 'marcach'
    si2 = SingularInfoC("cailleach", Gender.Fem)
    assert si2.genitive[0].value == 'caillí'
    assert si2.vocative[0].value == 'cailleach'
    assert si2.nominative[0].value == 'cailleach'
    assert si2.dative[0].value == 'cailleach'

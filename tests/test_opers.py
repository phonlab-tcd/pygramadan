from pygramadan.opers import *

def test_lenition():
    assert lenition("deas") == 'dheas'
    assert lenition("Deas") == 'Dheas'
    assert lenition("DEAS") == 'DHEAS'
    assert lenition("deas", 'd') == 'deas'
    assert lenition("Deas", 'd') == 'Deas'
    assert lenition("DEAS", 'd') == 'DEAS'
    assert lenition("djeas") == 'djeas'
    assert lenition("Djeas") == 'Djeas'
    assert lenition("DJEAS") == 'DJEAS'

def test_demutate():
    assert demutate('mballa') == 'balla'
    assert demutate('bhalla') == 'balla'
    assert demutate('gcat') == 'cat'
    assert demutate('chat') == 'cat'
    assert demutate('ndán') == 'dán'
    assert demutate('dhán') == 'dán'
    assert demutate('n-éan') == 'éan'
    assert demutate('nÉan') == 'Éan'
    assert demutate('t-éan') == 'éan'
    assert demutate('tÉan') == 'Éan'
    assert demutate("d'fhan") == 'fan'
    assert demutate("d'oscail") == 'oscail'
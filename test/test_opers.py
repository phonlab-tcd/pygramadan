from pygramadan.opers import lenition

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
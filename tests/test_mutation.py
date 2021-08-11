# coding=UTF-8
from pygramadan.mutation import *

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
    assert lenition("stad") == 'stad'
    assert lenition("slat") == 'shlat'

def test_eclipsis():
    assert eclipsis("balla") == 'mballa'
    assert eclipsis("cat") == 'gcat'
    assert eclipsis("dán") == 'ndán'
    assert eclipsis("geata") == 'ngeata'
    assert eclipsis("fuinneog") == 'bhfuinneog'
    assert eclipsis("dán", 'd') == 'dán'
    assert eclipsis("athair") == 'n-athair'
    assert eclipsis("Athair") == 'nAthair'

def test_uneclipse():
    assert uneclipse("mballa") == 'balla'
    assert uneclipse("gcat") == 'cat'
    assert uneclipse("nAthair") == 'Athair'
    assert uneclipse("bhFuinneog") == 'Fuinneog'

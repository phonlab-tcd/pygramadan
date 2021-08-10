from pygramadan.opers import *
from pygramadan.attributes import Mutation

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

def test_demutate():
    assert demutate('mballa') == 'balla'
    assert demutate('bhalla') == 'balla'
    assert demutate('gcat') == 'cat'
    assert demutate('chat') == 'cat'
    assert demutate('ndán') == 'dán'
    assert demutate('dhán') == 'dán'
    assert demutate('ngeata') == 'geata'
    assert demutate('gheata') == 'geata'
    assert demutate('n-éan') == 'éan'
    assert demutate('nÉan') == 'Éan'
    assert demutate('t-éan') == 'éan'
    assert demutate('tÉan') == 'Éan'
    assert demutate("d'fhan") == 'fan'
    assert demutate("d'oscail") == 'oscail'

def test_mutate():
    assert mutate(Mutation.Len1, "deas") == "dheas"
    assert mutate(Mutation.Len1D, "deas") == "dheas"
    assert mutate(Mutation.Len2, "deas") == "deas"
    assert mutate(Mutation.Len2D, "deas") == "deas"
    assert mutate(Mutation.Len1D, "foghlaim") == "d'fhoghlaim"
    assert mutate(Mutation.Len2D, "foghlaim") == "d'fhoghlaim"
    assert mutate(Mutation.Len3D, "foghlaim") == "d'fhoghlaim"
    assert mutate(Mutation.Len3, "Sagart") == "tSagart"
    assert mutate(Mutation.Len3D, "Sagart") == "tSagart"
    assert mutate(Mutation.Len3, "sagart") == "tsagart"
    assert mutate(Mutation.Len3D, "sagart") == "tsagart"
    assert mutate(Mutation.Len3, "stad") == "stad"
    assert mutate(Mutation.Len3D, "stad") == "stad"
    assert mutate(Mutation.Len3, "sneachta") == "tsneachta"
    assert mutate(Mutation.Len3D, "sneachta") == "tsneachta"
    assert mutate(Mutation.Ecl1, "doras") == "ndoras"
    assert mutate(Mutation.Ecl1x, "doras") == "ndoras"
    assert mutate(Mutation.Ecl2, "doras") == "doras"
    assert mutate(Mutation.Ecl3, "doras") == "doras"
    assert mutate(Mutation.Ecl1, "athair") == "n-athair"
    assert mutate(Mutation.Ecl1x, "athair") == "athair"
    assert mutate(Mutation.Ecl2, "athair") == "athair"
    assert mutate(Mutation.Ecl3, "athair") == "athair"
    assert mutate(Mutation.PrefH, "eagla") == "heagla"
    assert mutate(Mutation.PrefH, "stad") == "stad"
    assert mutate(Mutation.PrefT, "Éan") == "tÉan"
    assert mutate(Mutation.PrefT, "éan") == "t-éan"
    assert mutate(Mutation.PrefT, "stad") == "stad"

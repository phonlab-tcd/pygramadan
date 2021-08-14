# coding=UTF-8
from pygramadan.opers import broaden, demutate, mutate, is_slender, slenderise
from pygramadan.attributes import Mutation


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
    assert mutate(Mutation.Ecl1, "Athair") == "nAthair"
    assert mutate(Mutation.Ecl1, "sagart") == "sagart"
    assert mutate(Mutation.Ecl1x, "sagart") == "sagart"
    assert mutate(Mutation.Ecl2, "sagart") == "sagart"
    assert mutate(Mutation.Ecl3, "sagart") == "tsagart"
    assert mutate(Mutation.PrefH, "eagla") == "heagla"
    assert mutate(Mutation.PrefH, "stad") == "stad"
    assert mutate(Mutation.PrefT, "Éan") == "tÉan"
    assert mutate(Mutation.PrefT, "éan") == "t-éan"
    assert mutate(Mutation.PrefT, "stad") == "stad"


def test_is_slender():
    assert is_slender("lámh") is False
    assert is_slender("láimh") is True
    assert is_slender("lámha") is False


def test_slenderise():
    assert slenderise("féar") == "féir"
    assert slenderise("éan") == "éin"
    assert slenderise("cos") == "cois"
    assert slenderise("féir") == "féir"


def test_broaden():
    assert broaden("bóraíl") == "bóraíol"
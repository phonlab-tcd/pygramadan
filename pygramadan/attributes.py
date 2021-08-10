from enum import Enum

class Mutation(Enum):
    """
    Enum representing the type of mutation

    Note: as 'None' is a reserved word, Gramadán's None
    value has been changed to 'NoMut'
    """
    NoMut = 0
    Len1 = 1
    Len2 = 2
    Len3 = 3
    Ecl1 = 4
    Ecl1x = 5
    Ecl2 = 6
    Ecl3 = 7
    PrefT = 8
    PrefH = 9
    Len1D = 10
    Len2D = 11
    Len3D = 12

class Strength(Enum):
    Strong = 0
    Weak = 1

class Number(Enum):
    Sg = 0
    Pl = 1

class Gender(Enum):
    Masc = 0
    Fem = 1

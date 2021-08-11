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

    def __str__(self):
        if self.name == 'NoMut':
            return 'None'
        else:
            return self.name


class Strength(Enum):
    """
    Enum representing the strength of a wordform.
    'Strength' is a property of plural noun forms: strong plurals
    have the same form in nominative and genitive.
    The strength of the form influences the lenition of following
    adjectives.
    """
    Strong = 0
    Weak = 1


class Number(Enum):
    """
    Enum representing grammatical number (singular or plural)
    """
    Sg = 0
    Pl = 1


class Gender(Enum):
    """
    Enum representing grammatical gender (masculine or feminine)
    """
    Masc = 0
    Fem = 1

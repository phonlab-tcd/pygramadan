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


# The following are from Verbs.cs
class VerbTense(Enum):
    """
    Enum representing the "tense" of a verb
    (There is some overlap with mood and aspect here)
    """
    Past = 0
    PastCont = 1
    Pres = 2
    PresCont = 3
    Fut = 4
    Cond = 5


class VerbMood(Enum):
    """
    Enum representing the mood of a verb
    """
    Imper = 0
    Subj = 1


class VerbDependency(Enum):
    """
    Enum representing the dependency of a verb
    """
    Indep = 0
    Dep = 1


class VerbPerson(Enum):
    """
    Enum representing the person(/number) of a verb form
    """
    Base = 0
    Sg1 = 1
    Sg2 = 2
    Sg3 = 3
    Pl1 = 4
    Pl2 = 5
    Pl3 = 6
    Auto = 7


# From VP.cs
class VPTense(Enum):
    """
    Enum representing the "tense" of a verb form
    """
    Any = 0
    Past = 1
    PastCont = 2
    Pres = 3
    PresCont = 4
    Fut = 5
    Cond = 6


class VPMood(Enum):
    """
    Imperative or subjunctive
    """
    Imper = 0
    Subj = 1


class VPShape(Enum):
    """
    Declarative or interrogative
    """
    Any = 0
    Declar = 1
    Interrog = 2


class VPPerson(Enum):
    """
    Enum representing the person(/number/gender) of a verb form
    """
    Any = 0
    Sg1 = 1
    Sg2 = 2
    Sg3Masc = 3
    Sg3Fem = 4
    Pl1 = 5
    Pl2 = 6
    Pl3 = 7
    NoSubject = 8
    Auto = 9


class VPPolarity(Enum):
    """
    Positive/Negative/Either
    """
    Any = 0
    Pos = 1
    Neg = 2

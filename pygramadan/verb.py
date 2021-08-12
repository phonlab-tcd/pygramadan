from .attributes import Mutation as M, VerbPerson
from .attributes import VerbTense as VT
from .attributes import VerbDependency as VD
from .attributes import VerbMood as VM


class VerbTenseRule:
    def __init__(self,
                 particle: str = "",
                 mutation: M = M.NoMut,
                 tense: VT = VT.Pres,
                 dependency: VD = VD.Indep,
                 person: VerbPerson = VerbPerson.Base,
                 pronoun: str = "") -> None:
        self.particle = particle
        self.mutation = mutation
        self.tense = tense
        self.dependency = dependency
        self.person = person
        self.pronoun = pronoun
        
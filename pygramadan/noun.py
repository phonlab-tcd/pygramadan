from pygramadan.forms import Form

class Noun:
    def __str__(self) -> str:
        pass
    def __init__(self, file, 
                 definite: bool = False,
                 proper: bool = False,
                 immutable: bool = False,
                 disambig: str = ""
                 ) -> None:
        self.is_definite: bool = definite
        self.is_proper: bool = proper
        self.is_immutable: bool = immutable

        self.disambig: str = disambig

        self.sg_nom: list[Form]
        self.sg_gen: list[Form]
        self.sg_voc: list[Form]
        self.sg_dat: list[Form]

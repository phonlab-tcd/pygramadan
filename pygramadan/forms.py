from .attributes import Gender, Strength

class Form:
    def __init__(self, value: str) -> None:
        self.value: str = value
    
class FormSg(Form):
    def __init__(self, value: str, gender: Gender) -> None:
        self.value: str = value
        self.gender: Gender = gender

class FormPlGen(Form):
    def __init__(self, value: str, strength: Strength) -> None:
        self.value: str = value
        self.strength: Strength = strength

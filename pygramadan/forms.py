from .attributes import Gender, Strength


class Form:
    """A basic word form, containing only a string value"""
    def __init__(self, value: str) -> None:
        self.value: str = value


class FormSg(Form):
    """A singular noun form, containing a string value, and the grammatical gender of that form"""
    def __init__(self, value: str, gender: Gender) -> None:
        self.value: str = value
        self.gender: Gender = gender


class FormPlGen(Form):
    """A genitive plural form, containing a string value, and the 'strength' of the form"""
    def __init__(self, value: str, strength: Strength) -> None:
        self.value: str = value
        self.strength: Strength = strength

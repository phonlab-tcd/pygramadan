#from dataclasses import dataclass
from .attributes import Gender, Strength

#@dataclass
class Form:
    value: str

#@dataclass
class FormSg(Form):
    gender: Gender

#@dataclass
class FormPl(Form):
    strength: Strength

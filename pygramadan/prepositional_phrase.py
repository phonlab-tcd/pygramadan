from pygramadan.forms import Form, FormSg
from .attributes import Gender
from .opers import is_slender, is_slender_i, mutate, prefix
from .mutation import starts_vowel, starts_fvowel
from typing import List
import xml.etree.ElementTree as ET


class PP:
    def __init__(self) -> None:
        self.sg: List[FormSg] = []
        self.sg_art_n: List[FormSg] = []
        self.sg_art_s: List[FormSg] = []
        self.pl: List[Form] = []
        self.pl_art: List[Form] = []
        self.prep_id = ""
    
    def get_lemma(self) -> str:
        if len(self.sg) != 0:
            return self.sg[0].value
        elif len(self.sg_art_s) != 0:
            return self.sg_art_s[0].value
        elif len(self.sg_art_n) != 0:
            return self.sg_art_n[0].value
        elif len(self.pl) != 0:
            return self.pl[0].value
        elif len(self.pl_art) != 0:
            return self.pl_art[0].value
        else:
            return ""

    def get_identifier(self) -> str:
        return f"{self.get_lemma().replace(' ', '_')}_PP"

    def get_gender(self) -> Gender:
        if len(self.sg) != 0:
            return self.sg[0].gender
        elif len(self.sg_art_s) != 0:
            return self.sg_art_s[0].gender
        elif len(self.sg_art_n) != 0:
            return self.sg_art_n[0].gender
        else:
            return Gender.Masc

    def has_gender(self) -> bool:
        return len(self.sg) != 0 or len(self.sg_art_n) != 0 or len(self.sg_art_s) != 0

    def is_invalid(self) -> bool:
        total = len(self.sg)
        total += len(self.sg_art_s)
        total += len(self.sg_art_n)
        total += len(self.pl)
        total += len(self.pl_art)
        return total == 0

    def gramadan_string(self) -> str:
        return f"""
uatha, gan alt:                  {", ".join(self.sg)} 
uatha, alt, córas lárnach:       {", ".join(self.sg_art_s)} 
uatha, alt, córas an tséimhithe: {", ".join(self.sg_art_n)}
iolra, gan alt:                  {", ".join(self.pl)}
iolra, alt:                      {", ".join(self.pl_art)}
""".lstrip()

    

from pygramadan.forms import Form, FormSg
from .attributes import Gender, Mutation
from .opers import is_slender, is_slender_i, mutate, prefix
from .mutation import starts_vowel, starts_fvowel
from .preposition import Preposition
from .noun_phrase import NP
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

    def _init_prep_np(self, prep: Preposition, np: NP) -> None:
        self.prep_id = prep.get_identifier()
        def _ar_like(prp, bare_len = True):
            if bare_len:
                blmut = Mutation.Len3
            else:
                blmut = Mutation.NoMut
            for f in np.sg_dat:
                value = mutate(blmut, f.value)
                self.sg.append(FormSg(f'{prp} {value}', f.gender))
            for f in np.pl_dat:
                value = mutate(blmut, f.value)
                self.pl.append(Form(f'{prp} {value}'))
            for f in np.sg_dat_art_n:
                value = mutate(Mutation.Len3, f.value)
                self.sg_art_n.append(FormSg(f'{prp} an {value}', f.gender))
            for f in np.sg_dat_art_s:
                if f.gender == Gender.Fem:
                    mut = Mutation.Ecl3
                else:
                    mut = Mutation.Ecl2
                value = mutate(mut, f.value)
                self.sg_art_s.append(FormSg(f'{prp} an {value}', f.gender))
            for f in np.pl_dat_art:
                value = mutate(Mutation.PrefH, f.value)
                self.pl_art.append(Form(f'{prp} na {value}'))
        if self.prep_id == 'ag_prep':
            _ar_like('ag', False)
        if self.prep_id == 'ar_prep':
            _ar_like('ar')
        if self.prep_id == 'thar_prep':
            _ar_like('thar')


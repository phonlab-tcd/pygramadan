from pygramadan.forms import Form, FormSg
from .attributes import Gender, Mutation
from .opers import mutate
from .mutation import starts_bilabial, starts_vowel, starts_vowelfhx
from .preposition import Preposition
from .noun_phrase import NP
from .xml_helpers import formsg_node, formpl_node, write_sg, write_pl
from typing import List
import xml.etree.ElementTree as ET


class PP:
    def __init__(self,
                 source = None,
                 preposition: Preposition = None,
                 np: NP = None) -> None:
        self.sg: List[FormSg] = []
        self.sg_art_n: List[FormSg] = []
        self.sg_art_s: List[FormSg] = []
        self.pl: List[Form] = []
        self.pl_art: List[Form] = []
        self.prep_id = ""

        if source is not None:
            self.from_xml(source)
        elif preposition is not None and np is not None:
            self._init_prep_np(preposition, np)

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
            raise Exception('get_lemma: no form found suitable for lemma')

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

        def _ar_like(prp, bare_len = True, prpa = ""):
            if prpa == "":
                prpa = f'{prp} an'
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
                self.sg_art_n.append(FormSg(f'{prpa} {value}', f.gender))
            for f in np.sg_dat_art_s:
                if f.gender == Gender.Fem:
                    mut = Mutation.Ecl3
                else:
                    mut = Mutation.Ecl2
                value = mutate(mut, f.value)
                self.sg_art_s.append(FormSg(f'{prpa} {value}', f.gender))
            for f in np.pl_dat_art:
                value = mutate(Mutation.PrefH, f.value)
                self.pl_art.append(Form(f'{prp} na {value}'))

        def _de_do(prp):
            for f in np.sg_dat:
                value = mutate(Mutation.Len1, f.value)
                if starts_vowelfhx(value):
                    prpr = "d'"
                else:
                    prpr = f'{prp} '
                self.sg.append(FormSg(f'{prpr}{value}', f.gender))
            for f in np.pl_dat:
                value = mutate(Mutation.Len1, f.value)
                if starts_vowelfhx(value):
                    prpr = "d'"
                else:
                    prpr = f'{prp} '
                self.pl.append(Form(f'{prpr}{value}'))
            for f in np.sg_dat_art_n:
                value = mutate(Mutation.Len3, f.value)
                self.sg_art_n.append(FormSg(f'{prp}n {value}', f.gender))
            for f in np.sg_dat_art_s:
                if f.gender == Gender.Fem:
                    mut = Mutation.Len3
                else:
                    mut = Mutation.Len2
                value = mutate(mut, f.value)
                self.sg_art_s.append(FormSg(f'{prp}n {value}', f.gender))
            for f in np.pl_dat_art:
                value = mutate(Mutation.PrefH, f.value)
                self.pl_art.append(Form(f'{prp} na {value}'))

        if self.prep_id == 'ag_prep':
            _ar_like('ag', False)
        if self.prep_id == 'ar_prep':
            _ar_like('ar')
        if self.prep_id == 'thar_prep':
            _ar_like('thar')
        if self.prep_id == 'as_prep':
            _ar_like('as', False)
        if self.prep_id == 'chuig_prep':
            _ar_like('chuig', False)
        if self.prep_id == 'de_prep':
            _de_do('de')
        if self.prep_id == 'do_prep':
            _de_do('do')
        if self.prep_id == 'faoi_prep':
            _ar_like('faoi', True, 'faoin')
        if self.prep_id == 'i_prep':
            for f in np.sg_dat:
                if starts_vowel(f.value):
                    prpr = "in"
                    value = f.value
                else:
                    prpr = "i"
                    value = mutate(Mutation.Ecl1x, f.value)
                self.sg.append(FormSg(f'{prpr} {value}', f.gender))
            for f in np.pl_dat:
                if starts_vowel(f.value):
                    prpr = "in"
                    value = f.value
                else:
                    prpr = "i"
                    value = mutate(Mutation.Ecl1x, f.value)
                self.pl.append(Form(f'{prpr} {value}'))
            for f in np.sg_dat_art_n:
                value = mutate(Mutation.Len3, f.value)
                if starts_vowelfhx(value):
                    prpr = "san"
                else:
                    prpr = "sa"
                self.sg_art_n.append(FormSg(f'{prpr} {value}', f.gender))
            for f in np.sg_dat_art_s:
                if f.gender == Gender.Fem:
                    mut = Mutation.Len3
                else:
                    mut = Mutation.Len2
                value = mutate(mut, f.value)
                if starts_vowelfhx(value):
                    prpr = "san"
                else:
                    prpr = "sa"
                self.sg_art_s.append(FormSg(f'{prpr} {value}', f.gender))
            for f in np.pl_dat_art:
                value = mutate(Mutation.PrefH, f.value)
                self.pl_art.append(Form(f'sna {value}'))
        if self.prep_id == 'le_prep':
            print(np.__str__())
            for f in np.sg_dat:
                value = mutate(Mutation.PrefH, f.value)
                self.sg.append(FormSg(f'le {value}', f.gender))
            for f in np.pl_dat:
                value = mutate(Mutation.PrefH, f.value)
                self.pl.append(Form(f'le {value}'))
            for f in np.sg_dat_art_n:
                value = mutate(Mutation.Len3, f.value)
                self.sg_art_n.append(FormSg(f'leis an {value}', f.gender))
            for f in np.sg_dat_art_s:
                if f.gender == Gender.Fem:
                    mut = Mutation.Ecl3
                else:
                    mut = Mutation.Ecl2
                value = mutate(mut, f.value)
                self.sg_art_s.append(FormSg(f'leis an {value}', f.gender))
            for f in np.pl_dat_art:
                value = mutate(Mutation.PrefH, f.value)
                self.pl_art.append(Form(f'leis na {value}'))
        if self.prep_id == 'ó_prep':
            _ar_like('ó', True, 'ón')
        if self.prep_id == 'roimh_prep':
            _ar_like('roimh')
        if self.prep_id == 'trí_prep':
            _ar_like('trí', True, 'tríd an')
        if self.prep_id == 'um_prep':
            for f in np.sg_dat:
                if starts_bilabial(f.value):
                    mut = Mutation.Len1
                else:
                    mut = Mutation.NoMut
                value = mutate(mut, f.value)
                self.sg.append(FormSg(f'um {value}', f.gender))
            for f in np.pl_dat:
                if starts_bilabial(f.value):
                    mut = Mutation.Len1
                else:
                    mut = Mutation.NoMut
                value = mutate(mut, f.value)
                self.pl.append(Form(f'um {value}'))
            for f in np.sg_dat_art_n:
                value = mutate(Mutation.Len3, f.value)
                self.sg_art_n.append(FormSg(f'um an {value}', f.gender))
            for f in np.sg_dat_art_s:
                if f.gender == Gender.Fem:
                    mut = Mutation.Ecl3
                else:
                    mut = Mutation.Ecl2
                value = mutate(mut, f.value)
                self.sg_art_s.append(FormSg(f'um an {value}', f.gender))
            for f in np.pl_dat_art:
                value = mutate(Mutation.PrefH, f.value)
                self.pl_art.append(Form(f'um na {value}'))

    def from_xml(self, source) -> None:
        tree = ET.parse(source)
        root = tree.getroot()

        if 'prepNick' in root.attrib:
            self.prep_id = root.attrib['prepNick']

        formsg_node(root, './sg', self.sg)
        formsg_node(root, './sgArtN', self.sg_art_n)
        formsg_node(root, './sgArtS', self.sg_art_s)
        formpl_node(root, './pl', self.pl)
        formpl_node(root, './plArt', self.pl_art)

    def to_xml(self):
        props = {}
        props['default'] = self.get_lemma()
        props['prepNick'] = self.prep_id
        root = ET.Element('prepositionalPhrase', props)

        write_sg(self.sg, 'sg', root)
        write_sg(self.sg_art_s, 'sgArtS', root)
        write_sg(self.sg_art_n, 'sgArtN', root)
        write_pl(self.pl, 'pl', root)
        write_pl(self.pl_art, 'plArt', root)

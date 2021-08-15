from pygramadan.attributes import Gender, Mutation
from .forms import Form, FormSg
from .opers import mutate
from typing import List


class NP():
    def __init__(self) -> None:
        self.disambig: str = ""
        self.sg_nom: List[FormSg] = []
        self.sg_gen: List[FormSg] = []
        self.sg_dat: List[FormSg] = []
        self.sg_nom_art: List[FormSg] = []
        self.sg_gen_art: List[FormSg] = []
        self.sg_dat_art_n: List[FormSg] = []
        self.sg_dat_art_s: List[FormSg] = []
        self.pl_nom: List[Form] = []
        self.pl_gen: List[Form] = []
        # this is odd, because Noun only has plural vocative
        self.pl_dat: List[Form] = []
        self.pl_nom_art: List[Form] = []
        self.pl_gen_art: List[Form] = []
        self.pl_dat_art: List[Form] = []

        self.is_definite = False
        self.is_immutable = False
        self.force_nominative = False

    def __str__(self) -> str:
        return self._gramadan_string()

    def _gramadan_string(self) -> str:
        snom = 'sgNom: [' + '] ['.join([f.value for f in self.sg_nom]) + '] \n'
        sgen = 'sgGen: [' + '] ['.join([f.value for f in self.sg_gen]) + '] \n'
        pnom = 'plNom: [' + '] ['.join([f.value for f in self.pl_nom]) + '] \n'
        pgen = 'plGen: [' + '] ['.join([f.value for f in self.pl_gen]) + '] \n'
        snoma = 'sgNomArt: [' + '] ['.join([f.value for f in self.sg_nom]) + '] \n'
        sgena = 'sgGenArt: [' + '] ['.join([f.value for f in self.sg_gen]) + '] \n'
        pnoma = 'plNomArt: [' + '] ['.join([f.value for f in self.pl_nom]) + '] \n'
        pgena = 'plGenArt: [' + '] ['.join([f.value for f in self.pl_gen]) + '] \n'
        ngstr = snom + sgen + pnom + pgen + snoma + sgena + pnoma + pgena

        sdat = 'sgDat: [' + '] ['.join([f.value for f in self.sg_dat]) + '] \n'
        sdatan = 'sgDatArtN: [' + '] ['.join([f.value for f in self.sg_dat_art_n]) + '] \n'
        sdatas = 'sgDatArtS: [' + '] ['.join([f.value for f in self.sg_dat_art_s]) + '] \n'
        pdat = 'plDat: [' + '] ['.join([f.value for f in self.pl_dat]) + '] \n'
        pdata = 'plDatArt: [' + '] ['.join([f.value for f in self.pl_dat_art]) + '] \n'
        datstr = sdat + sdatan + sdatas + pdat + pdata
        return ngstr + '\n' + datstr

    def get_lemma(self) -> str:
        if len(self.sg_nom) != 0:
            return self.sg_nom[0].value
        elif len(self.sg_nom_art) != 0:
            return self.sg_nom_art[0].value
        elif len(self.pl_nom) != 0:
            return self.pl_nom[0].value
        elif len(self.pl_nom_art) != 0:
            return self.pl_nom_art[0].value
        else:
            raise Exception('get_lemma: no form found suitable for lemma')

    def get_identifier(self) -> str:
        disambig = ""
        if self.disambig != "":
            disambig = '_' + self.disambig
        return f"{self.get_lemma().replace(' ', '_')}_NP{disambig}"
    
    def has_gender(self) -> bool:
        return len(self.sg_nom) != 0 or len(self.sg_nom_art) != 0

    def get_gender(self) -> Gender:
        if len(self.sg_nom) != 0:
            return self.sg_nom[0].gender
        elif len(self.sg_nom_art) != 0:
            return self.sg_nom_art[0].gender
        else:
            return Gender.Masc

    def _init_explicit(self,
                       gender: Gender,
                       sg_nom: str,
                       sg_gen: str,
                       pl_nom: str,
                       pl_gen: str,
                       sg_dat_art_n: str):
        # without article
        self.sg_nom.append(FormSg(sg_nom, gender))
        # with article
        mut: Mutation = Mutation.PrefT if gender == Gender.Masc else Mutation.Len3
        value = mutate(mut, sg_nom)
        self.sg_nom.append(Form('an ' + value, gender))

        # without article
        # yes, sg_nom, not sg_gen
        self.sg_gen.append(FormSg(sg_nom, gender))
        # with article
        if gender == Gender.Masc:
            mut = Mutation.Len3
            article = 'an'
        else:
            mut = Mutation.PrefH
            article = 'na'
        value = mutate(mut, sg_gen)
        self.sg_gen.append(FormSg(f'{article} {value}', gender))

        # without article
        self.pl_nom.append(Form(pl_nom))

        # with article
        value = mutate(Mutation.PrefH, pl_nom)
        self.pl_nom.append(Form(f'na {value}'))

        # without article
        self.pl_gen.append(Form(pl_gen))

        # with article
        value = mutate(Mutation.Ecl1, pl_gen)
        self.pl_nom.append(Form(f'na {value}'))

        # without article
        self.sg_dat.append(FormSg(sg_nom, gender))

        # with article
        self.sg_dat_art_n.append(FormSg(sg_dat_art_n, gender))
        self.sg_dat_art_s.append(FormSg(sg_nom, Gender))

        mut = Mutation.PrefT if gender == Gender.Masc else Mutation.Len3
        value = mutate(mut, sg_nom)
        self.sg_nom_art.append(FormSg(value, gender))

        # without article
        self.pl_dat.append(Form(pl_nom))

        # with article
        self.pl_dat_art.append(Form(pl_nom))
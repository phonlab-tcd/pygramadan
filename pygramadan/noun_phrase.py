from pygramadan.adjective import Adjective
from pygramadan.noun import Noun
from pygramadan.attributes import Gender, Mutation
from .forms import Form, FormSg
from .opers import mutate, prefix
from typing import List


class NP():
    def __init__(self,
                 noun: Noun = None) -> None:
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

        if noun is not None:
            self._init_noun(noun)

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

    def _init_dict(self, props) -> None:
        _GENDER = {
            'masc': Gender.Masc,
            'fem': Gender.Fem
        }
        for key in ['gender', 'sg_nom', 'sg_gen', 'pl_nom', 'pl_gen', 'sg_dat_art_n']:
            if not key in props:
                raise Exception("Missing value for {key}")
        gender = _GENDER.get(props['gender'])
        if not gender:
            raise Exception("Unexpected value for gender: got {props['gender']}")
        self._init_explicit(gender,
                            props['sg_nom'],
                            props['sg_gen'],
                            props['pl_nom'],
                            props['pl_gen'],
                            props['sg_dat_art_n'])

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
        self.sg_nom_art.append(FormSg(f'an {value}', gender))

        # without article
        self.pl_dat.append(Form(pl_nom))

        # with article
        self.pl_dat_art.append(Form(pl_nom))

    def _init_noun(self, noun: Noun) -> None:
        self.is_definite = noun.is_definite
        self.is_immutable = noun.is_immutable

        for form in noun.sg_nom:
            self.sg_nom.append(FormSg(form.value, form.gender))
            if not noun.is_definite:
                if noun.is_immutable:
                    mut = Mutation.NoMut
                elif form.gender == Gender.Masc:
                    mut = Mutation.PrefT
                else:
                    mut = Mutation.Len3
                article = 'an'
                value = mutate(mut, form.value)
                self.sg_nom_art.append(FormSg(f'{article} {value}', form.gender))

        for form in noun.sg_gen:
            mut = Mutation.Len1 if noun.is_proper else Mutation.NoMut
            if noun.is_immutable:
                mut = Mutation.NoMut
            value = mutate(mut, form.value)
            self.sg_gen.append(FormSg(value, form.gender))
            if not noun.is_definite or noun.article_genitive:
                if noun.is_immutable:
                    mut = Mutation.NoMut
                elif form.gender == Gender.Masc:
                    mut = Mutation.Len3
                    article = 'an'
                else:
                    mut = Mutation.PrefH
                    article = 'na'
                value = mutate(mut, form.value)
                self.sg_gen_art.append(FormSg(f'{article} {value}', form.gender))

        for form in noun.pl_nom:
            self.pl_nom.append(Form(form.value))
            if not noun.is_definite:
                if noun.is_immutable:
                    mut = Mutation.NoMut
                else:
                    mut = Mutation.PrefH
                article = 'na'
                value = mutate(mut, form.value)
                self.pl_nom_art.append(Form(f'{article} {value}'))

        for form in noun.pl_gen:
            mut = Mutation.Len1 if noun.is_proper else Mutation.NoMut
            if noun.is_immutable:
                mut = Mutation.NoMut
            value = mutate(mut, form.value)
            self.pl_gen.append(Form(value))
            if not noun.is_definite or noun.article_genitive:
                if noun.is_immutable:
                    mut = Mutation.NoMut
                else:
                    mut = Mutation.Ecl1
                article = 'na'
                value = mutate(mut, form.value)
                self.pl_gen_art.append(Form(f'{article} {value}'))

        for form in noun.sg_dat:
            self.sg_dat.append(FormSg(form.value, form.gender))
            if not noun.is_definite:
                self.sg_dat_art_n.append(FormSg(form.value, form.gender))
                self.sg_dat_art_s.append(FormSg(form.value, form.gender))

        for form in noun.pl_nom:
            self.pl_dat.append(Form(form.value))
            if not noun.is_definite:
                self.pl_dat_art.append(Form(form.value))

    def _init_noun_adj(self, noun: Noun, mod: Adjective) -> None:
        # TODO(jim): #3 - move this copy to Noun
        if mod.prefix:
            prefixed: Noun = Noun(source=noun.to_xml())
            pfx = mod.get_lemma()
            for form in prefixed.sg_nom:
                form.value = prefix(pfx, form.value)
            for form in prefixed.sg_gen:
                form.value = prefix(pfx, form.value)
            for form in prefixed.sg_dat:
                form.value = prefix(pfx, form.value)
            for form in prefixed.sg_voc:
                form.value = prefix(pfx, form.value)
            for form in prefixed.pl_nom:
                form.value = prefix(pfx, form.value)
            for form in prefixed.pl_gen:
                form.value = prefix(pfx, form.value)
            for form in prefixed.pl_voc:
                form.value = prefix(pfx, form.value)
            for form in prefixed.count:
                form.value = prefix(pfx, form.value)
            np = NP(noun=prefixed)
            self.sg_nom = np.sg_nom
            self.sg_nom_art = np.sg_nom_art
            self.sg_gen = np.sg_gen
            self.sg_gen_art = np.sg_gen_art
            self.sg_dat = np.sg_dat
            self.sg_dat_art_n = np.sg_dat_art_n
            self.sg_dat_art_s = np.sg_dat_art_s
            self.pl_nom = np.pl_nom
            self.pl_nom_art = np.pl_nom_art
            self.pl_gen = np.pl_gen
            self.pl_gen_art = np.pl_gen_art
            self.pl_dat = np.pl_dat
            self.pl_dat_art = np.pl_dat_art
        else:
            self.is_definite = noun.is_definite
            self.is_immutable = noun.is_immutable
            self.force_nominative = True
            for form in noun.sg_nom:
                for modform in mod.sg_nom:
                    muta = Mutation.NoMut if form.gender == Gender.Masc else Mutation.Len1
                    adjval = mutate(muta, modform.value)
                    self.sg_nom.append(FormSg(f'{noun.value} {adjval}', form.gender))
                    if not noun.is_definite:
                        if form.gender == Gender.Masc:
                            mutn = Mutation.PrefT
                            muta = Mutation.NoMut
                        else:
                            mutn = Mutation.Len3
                            muta = Mutation.Len1
                        if noun.is_immutable:
                            mutn = Mutation.NoMut
                        nval = mutate(mutn, form.value)
                        aval = mutate(muta, modform.value)
                        self.sg_nom_art.append(FormSg(f'an {nval} {aval}', form.gender))

            for form in noun.sg_gen:
                if form.gender == Gender.Masc:
                    modforms = mod.sg_gen_masc
                else:
                    modforms = mod.sg_gen_fem
                for modform in modforms:
                    mutn = Mutation.Len1 if noun.is_proper else Mutation.NoMut
                    if noun.is_immutable:
                        mutn = Mutation.NoMut
                    muta = Mutation.Len1 if form.gender == Gender.Masc else Mutation.NoMut
                    nval = mutate(mutn, form.value)
                    aval = mutate(muta, modform.value)
                    self.sg_nom.append(FormSg(f'{nval} {aval}', form.gender))
                    if not noun.is_definite:
                        if form.gender == Gender.Masc:
                            mutn = Mutation.Len3
                            muta = Mutation.Len1
                            art = 'an'
                        else:
                            mutn = Mutation.PrefH
                            muta = Mutation.NoMut
                            art = 'na'
                        if noun.is_immutable:
                            mutn = Mutation.NoMut
                        nval = mutate(mutn, form.value)
                        aval = mutate(muta, modform.value)
                        self.sg_nom_art.append(FormSg(f'{art} {nval} {aval}', form.gender))

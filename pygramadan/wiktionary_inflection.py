from pygramadan.attributes import Gender, Strength
from .noun import Noun
from .forms import FormSg, Form, FormPlGen


def _extract_tpl_text(text: str) -> str:
    start = 0
    if '{{' in text:
        start = text.find('{{') + 2
    end = len(text)
    if '}}' in text:
        end = text.find('}}', start)
    return text[start:end]


def split_tpl_params(text: str):
    out = {}
    positional = []
    saw_eq = False
    text = _extract_tpl_text(text)
    pieces = text.split("|")
    out['name'] = pieces[0]
    for i in range(1, len(pieces)):
        if '=' in pieces[i]:
            saw_eq = True
            subspl = pieces[i].split('=')
            assert len(subspl) == 2

            out[subspl[0]] = subspl[1]
        else:
            if saw_eq:
                raise Exception(f"Error in template({text}): positional parameter {pieces[i]} follows named parameter {pieces[i-1]}")
            positional.append(pieces[i])
    out['positional'] = positional
    return out


def noun_f3(text: str) -> Noun:
    if 'ga-decl-f3' not in text:
        return None

    text = _extract_tpl_text(text)
    pieces = text.split('|')

    tpl = pieces[0]
    if tpl == 'ga-decl-f3-nopl':
        assert len(pieces) == 4
    else:
        assert len(pieces) == 5

    init = pieces[1]
    nom = init + pieces[2]
    gen = init + pieces[3]

    sg_nom = [FormSg(nom, Gender.Fem)]
    sg_gen = [FormSg(gen, Gender.Fem)]

    if tpl == 'ga-decl-f3':
        pl = init + pieces[4]
        pl_nom = [Form(pl)]
        pl_gen = [FormPlGen(pl, Strength.Strong)]

        return Noun(sg_nom=sg_nom, sg_gen=sg_gen, pl_nom=pl_nom, pl_gen=pl_gen, declension=2)
    else:
        return Noun(sg_nom=sg_nom, sg_gen=sg_gen, declension=2)


def noun_m3(text: str) -> Noun:
    if 'ga-decl-m3' not in text:
        return None

    text = _extract_tpl_text(text)
    pieces = text.split('|')

    tpl = pieces[0]
    if tpl == 'ga-decl-m3-nopl':
        assert len(pieces) == 4
    else:
        assert len(pieces) == 6 or len(pieces) == 5

    init = pieces[1]
    nom = init + pieces[2]
    gen = init + pieces[3]

    sg_nom = [FormSg(nom, Gender.Masc)]
    sg_gen = [FormSg(gen, Gender.Masc)]

    if tpl == 'ga-decl-m3':
        pl = init + pieces[4]
        pl_nom = [Form(pl)]

        if len(pieces) == 6:
            pl_gen = [FormPlGen(pl, Strength.Strong)]
        else:
            pl_gen = [FormPlGen(init + pieces[5], Strength.Weak)]
    else:
        pl_nom = None
        pl_gen = None

    return Noun(sg_nom=sg_nom, sg_gen=sg_gen, pl_nom=pl_nom, pl_gen=pl_gen, declension=3)


def noun_f4(text: str) -> Noun:
    if 'ga-decl-f4' not in text:
        return None

    tpldata = split_tpl_params(text)

    if tpldata["name"] == 'ga-decl-f4-nopl':
        assert len(tpldata["positional"]) == 2
    else:
        assert len(tpldata["positional"]) == 3

    init = tpldata["positional"][0]
    sg = init + tpldata["positional"][1]

    sg_nom = [FormSg(sg, Gender.Fem)]
    sg_gen = [FormSg(sg, Gender.Fem)]

    if tpldata["name"] == 'ga-decl-f4':
        pl = init + tpldata["positional"][2]
        pl_nom = [Form(pl)]
        pl_gen = [FormPlGen(pl, Strength.Strong)]

        return Noun(sg_nom=sg_nom, sg_gen=sg_gen, pl_nom=pl_nom, pl_gen=pl_gen, declension=4)
    else:
        return Noun(sg_nom=sg_nom, sg_gen=sg_gen, declension=4)


def noun_m4(text: str) -> Noun:
    if 'ga-decl-m4' not in text:
        return None

    tpldata = split_tpl_params(text)

    if tpldata["name"] == 'ga-decl-m4-nopl':
        assert len(tpldata["positional"]) == 2
    else:
        assert len(tpldata["positional"]) == 3

    init = tpldata["positional"][0]
    sg = init + tpldata["positional"][1]

    sg_nom = [FormSg(sg, Gender.Masc)]
    sg_gen = [FormSg(sg, Gender.Masc)]

    if tpldata["name"] == 'ga-decl-m4':
        pl = init + tpldata["positional"][2]
        pl_nom = [Form(pl)]
        pl_gen = [FormPlGen(pl, Strength.Strong)]

        return Noun(sg_nom=sg_nom, sg_gen=sg_gen, pl_nom=pl_nom, pl_gen=pl_gen, declension=4)
    else:
        return Noun(sg_nom=sg_nom, sg_gen=sg_gen, declension=4)


def noun_f2(text: str) -> Noun:
    if "ga-decl-f2" not in text:
        return None

    tpldata = split_tpl_params(text)
    assert len(tpldata["positional"]) == 3

    init = tpldata["positional"][0]

    nom = init + tpldata["positional"][1]
    gen = init + tpldata["positional"][2]

    sg_nom = [FormSg(nom, Gender.Fem)]
    sg_gen = [FormSg(gen, Gender.Fem)]

    if "pl" in tpldata:
        plnom = init + tpldata["pl"]
    else:
        plnom = nom + "a"
    
    if "genpl" in tpldata:
        plgen = init + tpldata["genpl"]
    else:
        plgen = nom

    if "dat" in tpldata:
        dat = init + tpldata["dat"]
        sg_dat = [FormSg(dat, Gender.Fem)]
    else:
        sg_dat = None

    if tpldata["name"] == "ga-decl-f2":
        if plnom == plgen:
            strength = Strength.Strong
        else:
            strength = Strength.Weak
        pl_nom = [Form(plnom)]
        pl_gen = [FormPlGen(plgen, strength)]
    else:
        pl_nom = None
        pl_gen = None

    return Noun(sg_nom=sg_nom, sg_gen=sg_gen, sg_dat=sg_dat, pl_nom=pl_nom, pl_gen=pl_gen, declension=2)


def noun_m2(text: str) -> Noun:
    if "ga-decl-m2" not in text:
        return None

    tpldata = split_tpl_params(text)
    assert len(tpldata["positional"]) == 3

    init = tpldata["positional"][0]

    nom = init + tpldata["positional"][1]
    gen = init + tpldata["positional"][2]

    sg_nom = [FormSg(nom, Gender.Masc)]
    sg_gen = [FormSg(gen, Gender.Masc)]

    if "pl" in tpldata:
        plnom = init + tpldata["pl"]
        plgen = init + tpldata["pl"]
    else:
        plnom = None
        plgen = None
    
    if "dat" in tpldata:
        dat = init + tpldata["dat"]
        sg_dat = [FormSg(dat, Gender.Masc)]
    else:
        sg_dat = None

    if plnom:
        if plnom == plgen:
            strength = Strength.Strong
        else:
            strength = Strength.Weak
        pl_nom = [Form(plnom)]
        pl_gen = [FormPlGen(plgen, strength)]
    else:
        pl_nom = None
        pl_gen = None

    return Noun(sg_nom=sg_nom, sg_gen=sg_gen, sg_dat=sg_dat, pl_nom=pl_nom, pl_gen=pl_gen, declension=2)


def noun_f5(text: str) -> Noun:
    if "ga-decl-f5" not in text:
        return None

    tpldata = split_tpl_params(text)
    if tpldata["name"] == "ga-decl-f5-nopl":
        assert len(tpldata["positional"]) == 3
    else:
        assert len(tpldata["positional"]) == 4

    init = tpldata["positional"][0]

    nom = init + tpldata["positional"][1]
    gen = init + tpldata["positional"][2]

    sg_nom = [FormSg(nom, Gender.Fem)]
    sg_gen = [FormSg(gen, Gender.Fem)]

    if len(tpldata["positional"]) == 4:
        plnom = init + tpldata["positional"][3]
    else:
        plnom = None
    
    if "genpl" in tpldata:
        if not plnom:
            raise Exception(f"Error in template: {text}: `genpl` specified without plural")
        plgen = init + tpldata["genpl"]
    elif plnom is not None:
        plgen = plnom
    else:
        plgen = None

    if "dat" in tpldata:
        dat = init + tpldata["dat"]
        sg_dat = [FormSg(dat, Gender.Fem)]
    else:
        sg_dat = None

    if tpldata["name"] == "ga-decl-f5":
        if plnom == plgen and plnom is not None:
            strength = Strength.Strong
        else:
            strength = Strength.Weak
        pl_nom = [Form(plnom)]
        pl_gen = [FormPlGen(plgen, strength)]
    else:
        pl_nom = None
        pl_gen = None

    return Noun(sg_nom=sg_nom, sg_gen=sg_gen, sg_dat=sg_dat, pl_nom=pl_nom, pl_gen=pl_gen, declension=5)


def noun_m5(text: str) -> Noun:
    if "ga-decl-m5" not in text:
        return None

    tpldata = split_tpl_params(text)
    assert len(tpldata["positional"]) == 4

    init = tpldata["positional"][0]

    nom = init + tpldata["positional"][1]
    gen = init + tpldata["positional"][2]

    sg_nom = [FormSg(nom, Gender.Masc)]
    sg_gen = [FormSg(gen, Gender.Masc)]

    if len(tpldata["positional"]) == 4:
        plnom = init + tpldata["positional"][3]
    else:
        plnom = None
    
    if "genpl" in tpldata:
        if not plnom:
            raise Exception(f"Error in template: {text}: `genpl` specified without plural")
        plgen = init + tpldata["genpl"]
    elif plnom is not None:
        plgen = plnom
    else:
        plgen = None

    if "dat" in tpldata:
        dat = init + tpldata["dat"]
        sg_dat = [FormSg(dat, Gender.Fem)]
    else:
        sg_dat = None

    if plnom == plgen and plnom is not None:
        strength = Strength.Strong
    else:
        strength = Strength.Weak
    pl_nom = [Form(plnom)]
    pl_gen = [FormPlGen(plgen, strength)]

    return Noun(sg_nom=sg_nom, sg_gen=sg_gen, sg_dat=sg_dat, pl_nom=pl_nom, pl_gen=pl_gen, declension=5)


def noun_m1(text: str) -> Noun:
    if "ga-decl-m1" not in text:
        return None

    tpldata = split_tpl_params(text)
    assert len(tpldata["positional"]) == 3

    init = tpldata["positional"][0]

    nom = init + tpldata["positional"][1]
    gen = init + tpldata["positional"][2]

    sg_nom = [FormSg(nom, Gender.Masc)]
    sg_gen = [FormSg(gen, Gender.Masc)]

    if tpldata["name"] == "ga-decl-m1":
        if "pl" in tpldata:
            plnom = init + tpldata["pl"]
        else:
            plnom = gen
        if "strong" in tpldata and tpldata["strong"] == "yes":
            strength = Strength.Strong
            plgen = plnom
        else:
            strength = Strength.Weak
            plgen = nom
        pl_nom = [Form(plnom)]
        pl_gen = [FormPlGen(plgen, strength)]
    else:
        pl_nom = None
        pl_gen = None


    return Noun(sg_nom=sg_nom, sg_gen=sg_gen, pl_nom=pl_nom, pl_gen=pl_gen, declension=1)


def noun_mV(text: str) -> Noun:
    if "ga-decl-m-V" not in text:
        return None

    tpldata = split_tpl_params(text)
    assert len(tpldata["positional"]) == 4

    nom = tpldata["positional"][0]
    gen = tpldata["positional"][1]

    sg_nom = [FormSg(nom, Gender.Masc)]
    sg_gen = [FormSg(gen, Gender.Masc)]

    if len(tpldata["positional"]) == 4:
        plnom = tpldata["positional"][2]
        plgen = tpldata["positional"][3]
    else:
        plnom = None
        plgen = None

    if "decl" in tpldata and tpldata["decl"] in "12345":
        decl = int(tpldata["decl"])
    else:
        decl = None

    if decl == 1:
        sg_voc = sg_gen
    else:
        sg_voc = sg_nom

    if "wv" in tpldata and tpldata["wv"] == "y":
        plvoc = nom + "a"
    else:
        plvoc = plnom

    if plnom == plgen and plnom is not None:
        strength = Strength.Strong
    else:
        strength = Strength.Weak
    pl_nom = [Form(plnom)]
    pl_gen = [FormPlGen(plgen, strength)]
    pl_voc = [Form(plvoc)]

    return Noun(sg_nom=sg_nom, sg_gen=sg_gen, sg_voc=sg_voc, pl_nom=pl_nom, pl_gen=pl_gen, pl_voc=pl_voc, declension=decl)


# TODO: no dative plural handling
def noun_irreg(text: str) -> Noun:
    if "ga-decl-m-irreg" not in text or "ga-decl-f-irreg" not in text:
        return None

    tpldata = split_tpl_params(text)

    if tpldata["name"] == "ga-decl-m-irreg-nopl" or tpldata["name"] == "ga-decl-f-irreg-nopl":
        assert len(tpldata["positional"]) == 3
    else:
        assert len(tpldata["positional"]) == 5

    init = tpldata["positional"][0]
    nom = init + tpldata["positional"][1]
    gen = init + tpldata["positional"][2]

    if tpldata["name"] == "ga-decl-m-irreg-nopl":
        gender = Gender.Masc
    else:
        gender = Gender.Fem

    sg_nom = [FormSg(nom, gender)]
    sg_gen = [FormSg(gen, gender)]

    if "dat" in tpldata:
        dat = init + tpldata["dat"]
        sg_dat = [FormSg(dat, gender)]
    else:
        sg_dat = None

    plnom = init + tpldata["positional"][3]
    plgen = init + tpldata["positional"][4]
    if plnom == plgen:
        strength = Strength.Strong
    else:
        strength = Strength.Weak

    if tpldata["name"] == "ga-decl-m-irreg" or tpldata["name"] == "ga-decl-f-irreg":
        pl_nom = [Form(plnom)]
        pl_gen = [FormPlGen(plgen, strength)]
    else:
        pl_nom = None
        pl_gen = None

    return Noun(sg_nom=sg_nom, sg_gen=sg_gen, sg_dat=sg_dat, pl_nom=pl_nom, pl_gen=pl_gen, declension=None)

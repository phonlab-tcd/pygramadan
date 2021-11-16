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


def noun_m4(text: str) -> Noun:
    if 'ga-decl-m4' not in text:
        return None

    text = _extract_tpl_text(text)
    pieces = text.split('|')

    tpl = pieces[0]
    if tpl == 'ga-decl-m4-nopl':
        assert len(pieces) == 3
    else:
        assert len(pieces) == 4

    init = pieces[1]
    sg = init + pieces[2]

    sg_nom = [FormSg(sg, Gender.Masc)]
    sg_gen = [FormSg(sg, Gender.Masc)]

    if tpl == 'ga-decl-m4':
        pl = init + pieces[3]
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


def noun_m1(text: str) -> Noun:
    if "ga-decl-m1" not in text:
        return None

    tpldata = split_tpl_params(text)
    assert len(tpldata["positional"]) == 4

    init = tpldata["positional"][0]

    nom = init + tpldata["positional"][1]
    gen = init + tpldata["positional"][2]

    sg_nom = [FormSg(nom, Gender.Fem)]
    sg_gen = [FormSg(gen, Gender.Fem)]

    if tpldata["name"] == "ga-decl-m1-nopl":
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

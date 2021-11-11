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

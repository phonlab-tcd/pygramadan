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
    else:
        pl_gen = None

    return Noun(sg_nom=sg_nom, sg_gen=sg_gen, pl_nom=pl_nom, pl_gen=pl_gen)
from pygramadan.noun import *
from pygramadan.forms import Form, FormSg, FormPlGen
from pygramadan.attributes import Gender, Strength


AINM_XML = """
<?xml version='1.0' encoding='utf-8'?>
<noun default="ainm" declension="4" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0">
  <sgNom default="ainm" gender="masc" />
  <sgGen default="ainm" gender="masc" />
  <plNom default="ainmneacha" />
  <plGen default="ainmneacha" strength="strong" />
</noun>
"""

def test_create():
    sg_nom = [FormSg("ainm", Gender.Masc)]
    sg_gen = [FormSg("ainm", Gender.Masc)]
    pl_nom = [Form("ainmneacha")]
    pl_gen = [FormPlGen("ainmneacha", Strength.Strong)]
    ainm = Noun(definite=False,
        proper=False,
        disambig="",
        declension=4,
        article_genitive=False,
        sg_nom=sg_nom,
        sg_gen=sg_gen,
        pl_nom=pl_nom,
        pl_gen=pl_gen
    )

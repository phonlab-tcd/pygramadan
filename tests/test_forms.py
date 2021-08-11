from pygramadan.forms import Form, FormPlGen, FormSg
from pygramadan.attributes import Gender, Strength

def test_forms():
    form = Form("sampla")
    assert form.value == "sampla" 

def test_formsg():
    formf = FormSg("traein", Gender.Fem)
    assert formf.value == "traein"
    assert formf.gender == Gender.Fem

def test_formpl():
    formpl = FormPlGen("traenacha", Strength.Strong)
    assert formpl.value == "traenacha"
    assert formpl.strength == Strength.Strong
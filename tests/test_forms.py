from pygramadan.forms import Form, FormPl, FormSg
from pygramadan.attributes import Gender, Strength

def test_forms():
    form = Form("sampla")
    assert form.value == "sampla" 
    formf = FormSg("traein", Gender.Fem)
    assert formf.value == "traein"
    assert formf.gender == Gender.Fem
    formpl = FormPl("traenacha", Strength.Strong)
    assert formpl.value == "traenacha"
    assert formpl.strength == Strength.Strong
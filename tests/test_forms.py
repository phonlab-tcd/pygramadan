from pygramadan.forms import Form, FormPl, FormSg
from pygramadan.attributes import Gender, Strength

# this is more about making sure that dataclasses works
# there isn't really anything to test otherwise
def test_forms():
    form = Form("sampla")
    assert form.value == "sampla" 

def test_formsg():
    formf = FormSg("traein", Gender.Fem)
    assert formf.value == "traein"
    assert formf.gender == Gender.Fem

def test_formpl():
    formpl = FormPl("traenacha", Strength.Strong)
    assert formpl.value == "traenacha"
    assert formpl.strength == Strength.Strong
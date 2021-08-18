from .attributes import Gender, Strength
import xml.etree.ElementTree as ET

def write_sg(inlist, name, root):
    for form in inlist:
        seprops = {}
        seprops['default'] = form.value
        seprops['gender'] = 'fem' if form.gender == Gender.Fem else 'masc'
        _ = ET.SubElement(root, name, seprops)


def write_pl(inlist, name, root):
    for form in inlist:
        seprops = {}
        seprops['default'] = form.value
        _ = ET.SubElement(root, name, seprops)


def write_pl_gen(inlist, name, root):
    for form in inlist:
        seprops = {}
        seprops['default'] = form.value
        seprops['strength'] = 'strong' if form.strength == Strength.Strong else 'weak'
        _ = ET.SubElement(root, name, seprops)

from .attributes import Gender, Strength
from pygramadan.forms import Form, FormSg, FormPlGen
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


def formsg_node(root, node, outlist):
    for form in root.findall(node):
        value = form.attrib.get('default')
        gender = Gender.Fem if form.attrib.get('gender') == 'fem' else Gender.Masc
        outlist.append(FormSg(value, gender))


def formpl_node(root, node, outlist):
    for form in root.findall(node):
        value = form.attrib.get('default')
        outlist.append(Form(value))


def formplgen_node(root, node, outlist):
    for form in root.findall(node):
        value = form.attrib.get('default')
        strength = Strength.Strong if form.attrib.get('strength') == 'strong' else Strength.Weak
        outlist.append(FormPlGen(value, strength))

# coding=UTF-8
from .attributes import Mutation
from .mutation import *
import re

def _safestart(text: str, piece: str, lc = False) -> bool:
    check = text if lc else text.lower()
    return len(text) >= len(piece) and check.startswith(piece)

def delenite(text: str) -> str:
    """
    Removes lenition from a word.

    :param text: the string to delenite
    :return: the string delenited, if applicable, otherwise unmodified
    """
    cons = "bcdfgmpst"
    lc = text.lower()
    if len(text) >= 2 and lc[0] in cons and lc[1] == 'h':
        return text[0] + text[2:]
    else:
        return text

def demutate(text: str) -> str:
    """
    Removes initial mutation from the input

    :param text: the string to demutate
    :return: the demutated string, or the unmodified string if no mutations apply
    """
    text = text[2:] if _safestart(text, "bhf") else text
    text = delenite(text)
    text = text[1:] if _safestart(text, "mb") else text
    text = text[1:] if _safestart(text, "gc") else text
    text = text[1:] if _safestart(text, "nd") else text
    text = text[1:] if _safestart(text, "ng") else text
    text = text[1:] if _safestart(text, "bp") else text
    text = text[1:] if _safestart(text, "ts") else text
    text = text[1:] if _safestart(text, "dt") else text
    text = delenite(text[2:]) if _safestart(text, "d'fh") else text
    lc = text.lower()
    text = text[2:] if len(lc) >= 3 and _safestart(text, "d'") and is_vowel(lc[2]) else text
    text = text[1:] if len(lc) >= 2 and lc[0] == 'h' and is_vowel(lc[1]) else text
    text = text[2:] if len(lc) >= 3 and _safestart(text, "n-") and is_vowel(lc[2]) else text
    # Gramadán doesn't do these
    text = text[2:] if len(lc) >= 3 and _safestart(text, "t-") and is_vowel(lc[2]) else text
    text = text[1:] if len(lc) >= 2 and lc[0] == 'n' and is_uppervowel(text[1]) else text
    text = text[1:] if len(lc) >= 2 and lc[0] == 't' and is_uppervowel(text[1]) else text
    return text

def eclipsis(text: str, restriction: str = "") -> str:
    mut = {
        'b': 'm',
        'c': 'g',
        'd': 'n',
        'f': 'bh',
        'g': 'n',
        'p': 'b',
        't': 'd'
    }
    firstl = text.lower()[0]
    if len(text) < 1:
        return text
    if is_uppervowel(text[0]):
        return "n" + text
    elif firstl == text[0] and is_vowel(text[0]):
        return "n-" + text
    elif firstl in mut and firstl not in restriction:
        return mut[firstl] + text
    else:
        return text


def mutate(mutation: Mutation, text: str) -> str:
    """
    Performs initial mutation on a word, according to
    mutation type.

    :param mutation: the type of mutation to perform
    :param text: the word to be mutated
    :return: the mutated word
    """
    lc = text.lower()
    if mutation == Mutation.Len1:
        return lenition(text)
    elif mutation == Mutation.Len1D:
        return d_lenition(text)
    elif mutation == Mutation.Len2:
        return lenition(text, 'dts')
    elif mutation == Mutation.Len2D:
        return d_lenition(text, 'dts')
    elif mutation == Mutation.Len3:
        if is_mutable_s(text):
            return 't' + text
        else:
            return lenition(text, 's')
    elif mutation == Mutation.Len3D:
        if is_mutable_s(text):
            return 't' + text
        else:
            return d_lenition(text, 's')
    elif mutation == Mutation.Ecl1:
        return eclipsis(text)
    elif mutation == Mutation.Ecl1x:
        if starts_vowel(text):
            return text
        else:
            return eclipsis(text)
    elif mutation == Mutation.Ecl2:
        if starts_vowel(text):
            return text
        else:
            return eclipsis(text, 'std')
    elif mutation == Mutation.Ecl3:
        if is_mutable_s(text):
            return 't' + text
        elif starts_vowel(text):
            return text
        else:
            return eclipsis(text, 'std')
    elif mutation == Mutation.PrefT:
        if starts_uppervowel(text):
            return 't' + text
        elif starts_vowel(text):
            return 't-' + text
        else:
            return text
    elif mutation == Mutation.PrefH:
        if starts_vowel(text):
            return 'h' + text
        else:
            return text

# FIXME: this is over-simplistic
def is_slender(text: str) -> bool:
    """Checks if a string ends with a slender vowel"""
    return re.search(r'[eiéí][^aeiouáéíóú]+$', text.lower()) != None


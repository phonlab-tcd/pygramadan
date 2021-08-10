# coding=UTF-8
from .attributes import Mutation

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

def is_vowel(char: str) -> bool:
    """
    Checks if the character is an Irish vowel (aeiouáéíóú).

    :param char: the character to check
    :return: true if the input is a single character, and is an Irish vowel
    """
    vowels = "aeiouáéíóú"
    return len(char) == 1 and char.lower()[0] in vowels

def is_uppervowel(char: str) -> bool:
    """
    Checks if the character is an uppercase Irish vowel (aeiouáéíóú).

    :param char: the character to check
    :return: true if the input is a single character, is uppercase, and is an Irish vowel
    """
    vowels = "AEIOUÁÉÍÓÚ"
    return len(char) == 1 and char[0] in vowels

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

def ends_dental(text: str) -> bool:
    """
    Checks if the word ends with a "dentals" consonant.
    ("DeNTalS" is a mnemonic to remember the consonants dnts)

    :param text: the string to check
    :return: true if the input ends with one of 'dnts'
    """
    return text.lower()[-1] in "dnts"

def starts_bilabial(text: str) -> bool:
    """
    Checks if the word starts with b, m, or p.

    :param text: the string to check
    :return: true if the input starts with one of 'bmp'
    """
    return len(text) > 0 and text.lower()[0] in "bmp"

def starts_vowel(text: str) -> bool:
    """
    Checks if the word starts with a vowel.

    :param text: the string to check
    :return: true if the input starts with a vowel
    """
    return len(text) > 0 and is_vowel(text[0])

def starts_vowelfhx(text: str) -> bool:
    """
    Checks if the word starts with a vowel, or 'fh', unless
    followed by l or r.

    :param text: the string to check
    :return: true if the input starts with a vowel or fh, but not fhl or fhr
    """
    lc = text.lower()
    if lc[0:3] == 'fhl' or lc[0:3] == 'fhr':
        return False
    else:
        return lc[0:2] == 'fh' or starts_vowel(text)

def starts_fvowel(text: str) -> bool:
    return len(text) > 0 and (is_vowel(text[0]) or text[0].lower() == 'f')

def is_mutable_s(text: str) -> bool:
    lc = text.lower()
    return len(lc) >= 2 and lc[0] == 's' and lc[1] in "rnlaeiouáéíóú"

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

def lenition(text: str, restriction: str = "") -> str:
    """
    Lenites the string.

    Lenition (séimhiú) is an initial mutation that applies to consonants.
    The orthographical realisation is via the insertion of 'h' after
    the initial consonant, if applicable: 'bcdfgmpst' are the letters that
    can be lenited; however, certain environments have restrictions on
    certain letters.

    :param text: the string to be lenited
    :param restriction: prevent lenition from being applied to these characters
    :return: the lenited string, if applicable, otherwise the value of text
    """
    def dolen(text: str) -> str:
        if text[0:2].isupper():
            return text[0] + 'H' + text[1:]
        else:
            return text[0] + 'h' + text[1:]
    if len(text) > 1 and text.lower()[1] == 'j':
        return text
    lc = text.lower()
    if len(text) >= 1 and lc[0] in "bcdfgmpt" and lc[0] not in restriction:
        return dolen(text)
    elif is_mutable_s(text) and 's' not in restriction:
        return dolen(text)
    else:
        return text

def mutate(mutation: Mutation, text: str) -> str:
    lc = text.lower()
    if mutation == Mutation.Len1:
        return lenition(text)
    elif mutation == Mutation.Len1D:
        if starts_vowel(text):
            return "d'" + text
        # Gramadán seems to not do lenition here?
        # it's probably handled later, but it's hard enough to read as is
        elif lc[0:1] == 'f':
            return "d'" + lenition(text)
        else:
            return lenition(text)
    elif mutation == Mutation.Len2:
        return lenition(text, 's')

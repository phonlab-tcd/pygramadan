# coding=UTF-8
"""
Helpers for mutation

The functions in Gramadán's Opers.cs are implemented in a
way that's quite specific to Gramadán. These functions
are intended to be more generally useful
"""
from typing import List


def safestart(text: str, piece: str, lc: bool = False) -> bool:
    """
    Checks if text starts with another, safely

    :param text: the string to check
    :param piece: the start string
    :return: true if text starts with piece
    """
    check = text if lc else text.lower()
    return len(text) >= len(piece) and check.startswith(piece)


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


def ends_dentals(text: str) -> bool:
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


def ends_vowel(text: str) -> bool:
    """
    Checks if the word ends with a vowel.

    :param text: the string to check
    :return: true if the input ends with a vowel
    """
    return len(text) > 0 and is_vowel(text[-1])


def starts_uppervowel(text: str) -> bool:
    """
    Checks if the word starts with an uppercase vowel.

    :param text: the string to check
    :return: true if the input starts with an uppercase  vowel
    """
    return len(text) > 0 and is_uppervowel(text[0])


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
    """
    Checks if the word starts with a vowel, or 'f'.

    :param text: the string to check
    :return: true if the input starts with a vowel or f
    """
    return len(text) > 0 and (is_vowel(text[0]) or text[0].lower() == 'f')


def starts_fthenvowel(text: str) -> bool:
    """
    Checks if the word starts with 'f' followed by a vowel

    :param text: the string to check
    :return: true if the input starts with f followed by a vowel
    """
    return text[0:1].lower() == 'f' and starts_vowel(text[1:])


def is_mutable_s(text: str) -> bool:
    """
    Checks if the word starts with a mutable 's'.
    ('s' is mutable when followed by a vowel, n, r, or l)

    :param text: the string to check
    :return: true if the input starts with a mutable s
    """
    lc = text.lower()
    return len(lc) >= 2 and lc[0] == 's' and lc[1] in "rnlaeiouáéíóú"


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

    >>> from pygramadan.mutation import lenition
    >>> lenition("cat")
    'chat'
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


def d_lenition(text, restriction=""):
    """
    Helper function for past tense mutation, where vowels are
    prefixed with "d'", and 'f' is lenited and prefixed with "d'"

    :param text: the string to be lenited
    :param restriction: prevent lenition from being applied to these characters
    :return: the lenited string, if applicable, otherwise the value of text

    >>> from pygramadan.mutation import d_lenition
    >>> d_lenition("fág")
    "d'fhág"
    """
    lc = text.lower()
    if starts_vowel(text):
        return "d'" + text
    elif lc[0:1] == 'f':
        return "d'" + lenition(text, restriction)
    else:
        return lenition(text, restriction)


def eclipsis(text: str, restriction: str = "") -> str:
    """
    Eclipses the string.

    Eclipsis (urú) is an initial mutation that applies to consonants and vowels.
    Voiced consonants and vowels are nasalised, while devoiced consonants are
    voiced. Orthographically, this is realised by prepending a consonant with
    the new phonetic value to the word.
    With consonants, this new value "eclipses" the original, e.g., 'c' is
    eclipsed as 'gc': only the 'g' is pronounced.

    :param text: the string to be eclipsed
    :param restriction: prevent eclipsis from being applied to these characters
    :return: the eclipsed string, if applicable, otherwise the value of text

    >>> from pygramadan.mutation import eclipsis
    >>> eclipsis("cat")
    'gcat'
    """
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


def unlenite(text: str) -> str:
    """
    Removes lenition from a word.

    :param text: the string to unlenite
    :return: the string with lenition removed, if applicable, otherwise unmodified

    >>> from pygramadan.mutation import unlenite
    >>> unlenite("chat")
    'cat'
    """
    cons = "bcdfgmpst"
    lc = text.lower()
    if len(text) >= 2 and lc[0] in cons and lc[1] == 'h':
        return text[0] + text[2:]
    else:
        return text


def _safestart_list(text: str, pieces: List[str], lc: bool = False) -> bool:
    """safestart() but for a list of pieces"""
    for piece in pieces:
        if safestart(text, piece, lc):
            return True
    return False


def uneclipse(text: str) -> str:
    """
    Removes eclipsis from a word.

    :param text: the string to uneclipse
    :return: the string with eclipse removed, if applicable, otherwise unmodified

    >>> from pygramadan.mutation import uneclipse
    >>> uneclipse("gcat")
    'cat'
    """
    if safestart(text, "bhf"):
        return text[2:]
    elif safestart(text, "n-") and is_vowel(text[2:3]):
        return text[2:]
    elif text[0:1] == 'n' and is_uppervowel(text[1:2]):
        return text[1:]
    elif _safestart_list(text, ["mb", "gc", "nd", "ng", "bp", "dt"]):
        return text[1:]
    else:
        return text

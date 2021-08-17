# coding=UTF-8
from .attributes import Mutation
from .mutation import ends_dentals, ends_vowel, is_mutable_s, is_vowel, safestart, unlenite, is_uppervowel
from .mutation import lenition, d_lenition, starts_vowel, starts_uppervowel, eclipsis
import re


def demutate(text: str) -> str:
    """
    Removes initial mutation from the input

    :param text: the string to demutate
    :return: the demutated string, or the unmodified string if no mutations apply
    """
    text = text[2:] if safestart(text, "bhf") else text
    text = unlenite(text)
    text = text[1:] if safestart(text, "mb") else text
    text = text[1:] if safestart(text, "gc") else text
    text = text[1:] if safestart(text, "nd") else text
    text = text[1:] if safestart(text, "ng") else text
    text = text[1:] if safestart(text, "bp") else text
    text = text[1:] if safestart(text, "ts") else text
    text = text[1:] if safestart(text, "dt") else text
    text = unlenite(text[2:]) if safestart(text, "d'fh") else text
    lc = text.lower()
    text = text[2:] if len(lc) >= 3 and safestart(text, "d'") and is_vowel(lc[2]) else text
    text = text[1:] if len(lc) >= 2 and lc[0] == 'h' and is_vowel(lc[1]) else text
    text = text[2:] if len(lc) >= 3 and safestart(text, "n-") and is_vowel(lc[2]) else text
    # Gramadán doesn't do these
    text = text[2:] if len(lc) >= 3 and safestart(text, "t-") and is_vowel(lc[2]) else text
    text = text[1:] if len(lc) >= 2 and lc[0] == 'n' and is_uppervowel(text[1]) else text
    text = text[1:] if len(lc) >= 2 and lc[0] == 't' and is_uppervowel(text[1]) else text
    return text


def mutate(mutation: Mutation, text: str) -> str:   # noqa: C901
    """
    Performs initial mutation on a word, according to
    mutation type.

    :param mutation: the type of mutation to perform
    :param text: the word to be mutated
    :return: the mutated word
    """
    if mutation == Mutation.NoMut:
        return text
    elif mutation == Mutation.Len1:
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


def is_slender(text: str) -> bool:
    """Checks if a string ends with a slender vowel"""
    return re.search(r'[eiéí][^aeiouáéíóú]+$', text.lower()) is not None


def is_slender_i(text: str) -> bool:
    """Checks if a string ends with a slender vowel"""
    return re.search(r'[ií][^aeiouáéíóú]+$', text.lower()) is not None


CONSONANTS = "bcdfghjklmnpqrstvwxz"
VOWELS = "aeiouáéíóú"
VOWELS_BROAD = "aouáóú"
VOWELS_SLENDER = "eiéí"


def slenderise(text: str) -> str:
    """
    Performs regular slenderisation (attenuation): if the base ends in a consonant,
    and if the vowel cluster immediately before this consonant ends in a broad vowel,
    then it changes this vowel cluster such that it ends in a slender vowel now.
    Note: a base that's already slender passes through unchanged.
    """
    vclust = {
        "ea": "i",
        "éa": "éi",
        "ia": "éi",
        "ío": "í",
        "io": "i",
        "iu": "i",
        "ae": "aei"
    }
    vclust_group = '(' + '|'.join(vclust.keys()) + ')'
    pat1 = '^(.*[' + CONSONANTS + '])?' + vclust_group + '([' + CONSONANTS + ']+)$'
    pat2 = '^' + vclust_group + '([' + CONSONANTS + ']+)$'
    # Addition: words like éan are not handled properly
    match = re.search(pat2, text)
    if match:
        return vclust[match.group(1)] + match.group(2)
    match = re.search(pat1, text)
    if match:
        return match.group(1) + vclust[match.group(2)] + match.group(3)
    # Base case: just add 'i'
    pat3 = '^(.*[' + VOWELS_BROAD + '])([' + CONSONANTS + ']+)$'
    match = re.search(pat3, text)
    if match:
        return match.group(1) + 'i' + match.group(2)
    return text


# This is the form that's called everywhere
# It doesn't actually seem to be used
def slenderise_target(text: str, target: str) -> str:
    """
    Performs irregular slenderization (attenuation): if the base ends in a
    consonant, and if the vowel cluster immediately before this consonant
    ends in a broad vowel, then it changes this vowel cluster into the target
    (the second argument).
    Note: if the target does not end in a slender vowel, then regular
    slenderisation is attempted instead.
    Note: a base that's already attenuated passes through unchanged.
    """
    if not re.search('[' + VOWELS_SLENDER + ']$', target):
        return slenderise(text)
    else:
        pat = '^(.*?)[' + VOWELS + ']*[' + VOWELS_BROAD + ']([' + CONSONANTS + ']+)$'
        match = re.search(pat, text)
        if match:
            return match.group(1) + target + match.group(2)
        else:
            return text


def broaden(text: str) -> str:
    """
    Performs regular broadening: if the base ends in a consonant, and if
    the vowel cluster immediately before this consonant ends in a slender
    vowel, then it changes this vowel cluster such that it ends in a broad
    vowel now.
	Note: a base that's already broad passes through unchanged.
    """
    vclust = {
        "ói": "ó",
        "ei": "ea",
        "éi": "éa",
        "i": "ea",
        "aí": "aío",
        "í": "ío",
        "ui": "o",
        "io": "ea"
    }
    vclust_group = '(' + '|'.join(vclust.keys()) + ')'
    pat1 = '^(.*[' + CONSONANTS + '])?' + vclust_group + '([' + CONSONANTS + ']+)$'
    pat2 = '^' + vclust_group + '([' + CONSONANTS + ']+)$'
    match = re.search(pat2, text)
    if match:
        return vclust[match.group(1)] + match.group(2)
    match = re.search(pat1, text)
    if match:
        return match.group(1) + vclust[match.group(2)] + match.group(3)
    # Base case: just remove 'i'
    pat3 = "^(.*)i([" + CONSONANTS + "]+)$"
    match = re.search(pat3, text)
    if match:
        return match.group(1) + match.group(2)
    return text


def broaden_target(text: str, target: str) -> str:
    """
    Performs irregular broadening: if the base ends in a consonant, and if
    the vowel cluster immediately before this consonant ends in a slender
    vowel, then it changes this vowel cluster into the target (the second
    argument).
	Note: if the target does not end in a broad vowel, then regular
    broadening is attempted instead.
	Note: a base that's already broad passes through unchanged.
    """
    if not re.search('[' + VOWELS_BROAD + ']$', target):
        return broaden(text)
    else:
        pat = '^(.*?)[' + VOWELS + ']*[' + VOWELS_SLENDER + ']([' + CONSONANTS + ']+)$'
        match = re.search(pat, text)
        if match:
            return match.group(1) + target + match.group(2)
        else:
            return text


def devoice(text: str) -> str:
    """
    "If the final consonant cluster consists of two consonants that differ
    in voicing, and if neither one of them is "l", "n" or "r", then devoices
    the second one."
    In reality, this just replaces 'sd' at the end of a word with 'st'.
    """
    if text.endswith('sd'):
        return text[0:-2] + 'st'
    else:
        return text


def deduplicate(text: str) -> str:
    """Reduces any duplicated consonants at the end into a single consonant."""
    # pat = "^.*[" + CONSONANTS + "][" + CONSONANTS + "]$"
    ult = text[-1:]
    pult = text[-2:-1]
    if ult in CONSONANTS and pult in CONSONANTS and ult == pult:
        return text[0:-1]
    else:
        return text


def syncopate(text: str) -> str:
    """
    Performs syncopation by removing the final vowel cluster, then 
    deduplicates and devoices the consonant cluster at the end.
    Note: called 'syncope' in Gramadán
    """
    pat = "^(.*[" + CONSONANTS + "])?[" + VOWELS + "]+([" + CONSONANTS + "]+)$"
    match = re.search(pat, text)
    if match:
        return devoice(deduplicate(match.group(1) + match.group(2)))
    else:
        return text


def highlight_mutations(text: str, bayse: str = "") -> str:
    text = re.sub(r"(^| )([cdfgmpst])(h)", r"\1\2<u class='lenition'>\3</u>", text, flags=re.I)
    text = re.sub(r"(^| )(b)(h)([^f])", r"\1\2<u class='lenition'>\3</u>\4", text, flags=re.I)
    text = re.sub(r"(^| )(t)(s)", r"\1<u class='lenition'>\2</u>\3", text, flags=re.I)
    text = re.sub(r"(^| )(m)(b)", r"\1<u class='eclipsis'>\2</u>\3", text, flags=re.I)
    text = re.sub(r"(^| )(g)(c)", r"\1<u class='eclipsis'>\2</u>\3", text, flags=re.I)
    text = re.sub(r"(^| )(n)(d)", r"\1<u class='eclipsis'>\2</u>\3", text, flags=re.I)
    text = re.sub(r"(^| )(bh)(f)", r"\1<u class='eclipsis'>\2</u>\3", text, flags=re.I)
    text = re.sub(r"(^| )(n)(g)", r"\1<u class='eclipsis'>\2</u>\3", text, flags=re.I)
    text = re.sub(r"(^| )(b)(p)", r"\1<u class='eclipsis'>\2</u>\3", text, flags=re.I)
    text = re.sub(r"(^| )(d)(t)", r"\1<u class='eclipsis'>\2</u>\3", text, flags=re.I)
    text = re.sub(r"(^| )(n-)([aeiouáéíóú])", r"\1<u class='eclipsis'>\2</u>\3", text)
    if not bayse.startswith("n"):
        text = re.sub(r"(^| )(n)([AEIOUÁÉÍÓÚ])", r"\1<u class='eclipsis'>\2</u>\3", text)
    if not bayse.startswith("t-"):
        text = re.sub(r"(^| )(t-)([aeiouáéíóú])", r"\1<u class='lenition'>\2</u>\3", text)
    if not bayse.startswith("t"):
        text = re.sub(r"(^| )(t)([AEIOUÁÉÍÓÚ])", r"\1<u class='lenition'>\2</u>\3", text)
    if not bayse.startswith("h"):
        text = re.sub(r"(^| )(h)([aeiouáéíóú])", r"\1<u class='lenition'>\2</u>\3", text, flags=re.I)
    return text


def prefix(prefix: str, body: str) -> str:
    m = Mutation.Len1
    if ends_dentals(prefix):
        m = Mutation.Len2
    if prefix[-1] == body[0]:
        prefix += '-'
    if ends_vowel(prefix) and starts_vowel(body):
        prefix += '-'
    if body[0].isupper():
        prefix = prefix[0].upper() + prefix[1:]
        if not prefix[-1] == '-':
            prefix += '-'
    return prefix + mutate(m, body)

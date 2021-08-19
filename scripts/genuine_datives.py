import argparse
from pygramadan.noun import Noun
from pygramadan.opers import slenderise
from pygramadan.mutation import lenition, eclipsis
from pathlib import Path
import sys
"""
The purpose of this script is to generate pairs of nominative and dative;
the dative is still used in West Munster, while it often replaces the
nominative in East Munster and parts of Connacht (e.g., Cois Fharraige).

46. The Dative case singular is the same as the nominative singular, except
(1) in the 2nd declension, when the noun ends in a broad consonant;
(2) in most of the nouns of the 5th declension.
https://en.wikisource.org/wiki/Graim%C3%A9ar_na_Gaedhilge/Part_II_Chapter_II
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bunamo", type=str, help="path to BuNaMo")
    parser.add_argument("-m", "--mutate", type=bool, help="if set, also mutate the words")
    args = parser.parse_args()
    if args.bunamo is None:
        sys.exit('--bunamo option not set')
    bunamo = Path(args.bunamo)
    if not bunamo.is_dir():
        sys.exit(f'path "{args.bunamo}" is not a directory')
    noun_dir = bunamo / 'noun'
    if not noun_dir.is_dir():
        sys.exit(f'"{args.bunamo}" does not contain noun/ directory')

    for noun_file in noun_dir.glob('*[25]*.xml'):
        n = Noun(source=noun_file)
        lemma = n.get_lemma()
        if lemma.endswith('ach'):
            continue
        slender = slenderise(lemma)
        if lemma != slender:
            print(f'{lemma}\t{slender}')
            if args.mutate:
                lenlem = lenition(lemma)
                lensl = lenition(slender)
                if lenlem != lemma:
                    print(f'{lenlem}\t{lensl}')
                ecllem = eclipsis(lemma)
                eclsl = eclipsis(slender)
                if ecllem != lemma:
                    print(f'{ecllem}\t{eclsl}')


if __name__ == "__main__":
    main()

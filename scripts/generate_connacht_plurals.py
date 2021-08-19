import argparse
from pygramadan.noun import Noun
from pathlib import Path
import sys
"""
Connacht plurals for -acha/-anna are -achaí/-annaí
(derived from the old dative plurals -achaibh/-annaibh)
Even if these forms are to be included in the pronunciation
lexicon as variants, these forms are easier to generate
with G2P as they map to the correct vowel.
"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bunamo", type=str, help="path to BuNaMo")
    args = parser.parse_args()
    if args.bunamo is None:
        sys.exit('--bunamo option not set')
    bunamo = Path(args.bunamo)
    if not bunamo.is_dir():
        sys.exit(f'path "{args.bunamo}" is not a directory')
    noun_dir = bunamo / 'noun'
    if not noun_dir.is_dir():
        sys.exit(f'"{args.bunamo}" does not contain noun/ directory')

    for noun_file in noun_dir.glob('*.xml'):
        n = Noun(source=noun_file)
        if len(n.pl_nom) > 0 and len(n.pl_gen) > 0 and n.pl_nom[0].value == n.pl_gen[0].value:
            for form in n.pl_nom:
                if form.value.endswith('acha') or form.value.endswith('anna'):
                    print(f'{form.value}\t{form.value}í')


if __name__ == "__main__":
    main()

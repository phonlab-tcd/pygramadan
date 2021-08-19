import argparse
from pygramadan.noun import Noun
from pygramadan.opers import slenderise
from pathlib import Path
import sys


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

    for noun_file in noun_dir.glob('*2*.xml'):
        n = Noun(source=noun_file)
        lemma = n.get_lemma()
        slender = slenderise(lemma)
        if lemma != slender:
            print(f'{lemma}\t{slender}')


if __name__ == "__main__":
    main()

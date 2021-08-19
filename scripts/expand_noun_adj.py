import argparse
from pygramadan.noun import Noun
from pygramadan.adjective import Adjective
from pygramadan.noun_phrase import NP
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bunamo", type=str, help="path to BuNaMo")
    parser.add_argument('noun', type=str, help='the noun to inflect')
    parser.add_argument('adj', type=str, help='the adjective to inflect')
    args = parser.parse_args()
    if args.bunamo is None:
        sys.exit('--bunamo option not set')
    bunamo = Path(args.bunamo)
    if not bunamo.is_dir():
        sys.exit(f'path "{args.bunamo}" is not a directory')
    noun_dir = bunamo / 'noun'
    if not noun_dir.is_dir():
        sys.exit(f'"{args.bunamo}" does not contain noun/ directory')
    adj_dir = bunamo / 'adjective'
    if not adj_dir.is_dir():
        sys.exit(f'"{args.bunamo}" does not contain adjective/ directory')

    noun_pat = args.noun + '_' + '*.xml'
    adj_pat = args.adj + '_' + '*.xml'
    for noun_file in noun_dir.glob(noun_pat):
        for adj_file in adj_dir.glob(adj_pat):
            n = Noun(source=noun_file)
            a = Adjective(source=adj_file)
            np = NP(noun=n, adjective=a)
            print(f'{n.get_identifier()}\t{a.get_identifier()}')
            print(np.__str__())

if __name__ == "__main__":
    main()

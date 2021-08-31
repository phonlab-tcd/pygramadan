import argparse
from pygramadan.noun import Noun
from pygramadan.adjective import Adjective
from pathlib import Path
import json
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
    adj_dir = bunamo / 'adjective'
    if not adj_dir.is_dir():
        sys.exit(f'"{args.bunamo}" does not contain adjective/ directory')
    verb_dir = bunamo / 'verb'
    if not verb_dir.is_dir():
        sys.exit(f'"{args.bunamo}" does not contain verb/ directory')
    prep_dir = bunamo / 'preposition'
    if not prep_dir.is_dir():
        sys.exit(f'"{args.bunamo}" does not contain preposition/ directory')

    nouns = {}
    for noun_file in noun_dir.glob('*.xml'):
        cur_noun = Noun(source=noun_file)
        cur_lem = cur_noun.get_lemma()
        if cur_lem not in nouns:
            nouns[cur_lem] = set()
        for form in cur_noun.get_unique_forms():
            if form != cur_lem:
                nouns[cur_lem].add(form)
    for noun in nouns.keys():
        if len(nouns[noun]) == 1:
            nouns[noun] = list(nouns[noun])[0]
        else:
            nouns[noun] = list(nouns[noun])
    
    with open('ga_lemma_lookup_noun.json', 'w') as out:
        json.dump(nouns, out)


if __name__ == "__main__":
    main()

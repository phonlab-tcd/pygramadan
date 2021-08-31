import argparse
from pygramadan.noun import Noun
from pygramadan.adjective import Adjective
from pathlib import Path
import json
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bunamo", type=str, help="path to BuNaMo")
    parser.add_argument("-s", "--skiplemma", type=bool, help="skip lemmas")
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

    noun_forms = {}
    for noun_file in noun_dir.glob('*.xml'):
        cur_noun = Noun(source=noun_file)
        cur_lem = cur_noun.get_lemma()
        for form in cur_noun.get_unique_forms():
            if form not in noun_forms:
                noun_forms[form] = set()
            if args.skiplemma and form != cur_lem:
                noun_forms[form].add(cur_lem)
    for noun in noun_forms.keys():
        if len(noun_forms[noun]) == 0:
            continue
        elif len(noun_forms[noun]) == 1:
            noun_forms[noun] = list(noun_forms[noun])[0]
        else:
            noun_forms[noun] = list(noun_forms[noun])
    
    with open('ga_lemma_lookup_noun.json', 'w') as out:
        json.dump(noun_forms, out, indent=2)


if __name__ == "__main__":
    main()
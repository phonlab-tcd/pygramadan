import argparse
from pygramadan.verb import Verb
from pygramadan.preposition import Preposition
from pygramadan.possessive import Possessive
from pygramadan.noun import Noun
from pygramadan.adjective import Adjective
from pathlib import Path
import json
import sys


def process_nouns(args, noun_dir):
    noun_forms = {}
    for noun_file in noun_dir.glob('*.xml'):
        cur_noun = Noun(source=noun_file)
        cur_lem = cur_noun.get_lemma()
        for form in cur_noun.get_unique_forms():
            if (args.skiplemma and form != cur_lem) or not args.skiplemma:
                if form not in noun_forms:
                    noun_forms[form] = set()
                noun_forms[form].add(cur_lem)
    delkeys = []
    for noun in noun_forms.keys():
        if len(noun_forms[noun]) == 0:
            delkeys.append(noun_forms[noun])
        if len(noun_forms[noun]) == 1:
            noun_forms[noun] = list(noun_forms[noun])[0]
        else:
            noun_forms[noun] = list(noun_forms[noun])

    for dk in delkeys:
        del noun_forms[dk]

    with open('ga_lemma_lookup_noun.json', 'w') as out:
        json.dump(noun_forms, out, indent=2)

    noun_forms.clear()


def process_adjectives(args, adj_dir):
    adj_forms = {}
    for adj_file in adj_dir.glob('*.xml'):
        cur_adj = Adjective(source=adj_file)
        cur_lem = cur_adj.get_lemma()
        for form in cur_adj.get_unique_forms():
            if (args.skiplemma and form != cur_lem) or not args.skiplemma:
                if form not in adj_forms:
                    adj_forms[form] = set()
                adj_forms[form].add(cur_lem)
    delkeys = []
    for noun in adj_forms.keys():
        if len(adj_forms[noun]) == 0:
            delkeys.append(adj_forms[noun])
        if len(adj_forms[noun]) == 1:
            adj_forms[noun] = list(adj_forms[noun])[0]
        else:
            adj_forms[noun] = list(adj_forms[noun])

    for dk in delkeys:
        del adj_forms[dk]

    with open('ga_lemma_lookup_adj.json', 'w') as out:
        json.dump(adj_forms, out, indent=2)

    adj_forms.clear()


def process_possessives(args, poss_dir):
    poss_forms = {}
    for poss_file in poss_dir.glob('*.xml'):
        cur_poss = Possessive(source=poss_file)
        cur_lem = cur_poss.get_lemma()
        for form in cur_poss.get_unique_forms():
            if (args.skiplemma and form != cur_lem) or not args.skiplemma:
                if form not in poss_forms:
                    poss_forms[form] = set()
                poss_forms[form].add(cur_lem)
    delkeys = []
    for noun in poss_forms.keys():
        if len(poss_forms[noun]) == 0:
            delkeys.append(poss_forms[noun])
        if len(poss_forms[noun]) == 1:
            poss_forms[noun] = list(poss_forms[noun])[0]
        else:
            poss_forms[noun] = list(poss_forms[noun])

    for dk in delkeys:
        del poss_forms[dk]

    with open('ga_lemma_lookup_poss.json', 'w') as out:
        json.dump(poss_forms, out, indent=2)

    poss_forms.clear()


def process_prepositions(args, prep_dir):
    prep_forms = {}
    for prep_file in prep_dir.glob('*.xml'):
        cur_poss = Preposition(source=prep_file)
        cur_lem = cur_poss.get_lemma()
        for form in cur_poss.get_unique_forms():
            if (args.skiplemma and form != cur_lem) or not args.skiplemma:
                if form not in prep_forms:
                    prep_forms[form] = set()
                prep_forms[form].add(cur_lem)
    delkeys = []
    for noun in prep_forms.keys():
        if len(prep_forms[noun]) == 0:
            delkeys.append(prep_forms[noun])
        if len(prep_forms[noun]) == 1:
            prep_forms[noun] = list(prep_forms[noun])[0]
        else:
            prep_forms[noun] = list(prep_forms[noun])

    for dk in delkeys:
        del prep_forms[dk]

    with open('ga_lemma_lookup_prep.json', 'w') as out:
        json.dump(prep_forms, out, indent=2)

    prep_forms.clear()


def process_verbs(args, verb_dir):
    verb_forms = {}
    for verb_file in verb_dir.glob('*.xml'):
        cur_poss = Verb(source=verb_file)
        cur_lem = cur_poss.get_lemma()
        for form in cur_poss.get_unique_forms():
            if (args.skiplemma and form != cur_lem) or not args.skiplemma:
                if form not in verb_forms:
                    verb_forms[form] = set()
                verb_forms[form].add(cur_lem)
    delkeys = []
    for noun in verb_forms.keys():
        if len(verb_forms[noun]) == 0:
            delkeys.append(verb_forms[noun])
        if len(verb_forms[noun]) == 1:
            verb_forms[noun] = list(verb_forms[noun])[0]
        else:
            verb_forms[noun] = list(verb_forms[noun])

    for dk in delkeys:
        del verb_forms[dk]

    with open('ga_lemma_lookup_verb.json', 'w') as out:
        json.dump(verb_forms, out, indent=2)

    verb_forms.clear()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bunamo", type=str, help="path to BuNaMo")
    parser.add_argument("-s", "--skiplemma", type=bool, default=False, help="skip lemmas")
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
    poss_dir = bunamo / 'possessive'
    if not poss_dir.is_dir():
        sys.exit(f'"{args.bunamo}" does not contain possessive/ directory')

    process_nouns(args, noun_dir)
    process_adjectives(args, adj_dir)
    process_possessives(args, poss_dir)
    process_prepositions(args, prep_dir)
    process_verbs(args, verb_dir)


if __name__ == "__main__":
    main()

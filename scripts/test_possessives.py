import argparse
from pygramadan.noun import Noun
from pygramadan.possessive import Possessive
from pygramadan.noun_phrase import NP
from pathlib import Path
import sys


_NOUNS = [
    "árasán_masc1.xml",
    "bó_fem.xml",
    "comhlacht_masc3.xml",
    "dealbh_fem2.xml",
    "éiceachóras_masc1.xml",
    "francfurtar_masc1.xml",
    "fliúit_fem2.xml",
    "fadhb_fem2.xml",
    "fobhríste_masc4.xml",
    "garáiste_masc4.xml",
    "haematóma_masc4.xml",
    "iasacht_fem3.xml",
    "jab_masc4.xml",
    "leabharlann_fem2.xml",
    "máthair_fem5.xml",
    "nóta_masc4.xml",
    "ócáid_fem2.xml",
    "pacáiste_masc4.xml",
    "rás_masc3.xml",
    "sobaldráma_masc4.xml",
    "sábh_masc1.xml",
    "stábla_masc4.xml",
    "sráid_fem2.xml",
    "tábhairne_masc4.xml",
    "ubh_fem2.xml",
    "x-gha_masc4.xml",
    "zombaí_masc4.xml"
]


_POSS = [
    "mo_poss.xml",
    "do_poss.xml",
    "a_poss_masc.xml",
    "a_poss_fem.xml",
    "ár_poss.xml",
    "bhur_poss.xml",
    "a_poss_pl.xml"
]


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
    poss_dir = bunamo / 'possessive'
    if not poss_dir.is_dir():
        sys.exit(f'"{args.bunamo}" does not contain possessive/ directory')
    noun_files = [noun_dir / x for x in _NOUNS]
    poss_files = [poss_dir / x for x in _POSS]
    nouns = [Noun(source=f) for f in noun_files]
    poss = [Possessive(source=f) for f in poss_files]

    for noun in nouns:
        for p in poss:
            np = NP(noun=noun, possessive=p)
            print(f'{p.get_identifier()}\t{np.sg_nom[0].value}\t{np.sg_gen[0].value}\t{np.pl_nom[0].value}\t{np.pl_gen[0].value}')

if __name__ == "__main__":
    main()
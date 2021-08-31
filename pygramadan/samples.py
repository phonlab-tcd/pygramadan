from tests.test_noun import AINM_XML_HEADER


_HEADER = """
<?xml version='1.0' encoding='utf-8'?>
"""

BEAG_XML = """
<adjective default="beag" declension="1" disambig="" isPre="0">
  <sgNom default="beag" />
  <sgGenMasc default="big" />
  <sgGenFem default="bige" />
  <plNom default="beaga" />
  <graded default="lú" />
  <abstractNoun default="laghad" />
</adjective>
"""

BEAG_XML_HEADER = _HEADER + BEAG_XML


AINM_XML = """
<noun default="ainm" declension="4" disambig="" isProper="0" isDefinite="0" allowArticledGenitive="0" isImmutable="0">
  <sgNom default="ainm" gender="masc" />
  <sgGen default="ainm" gender="masc" />
  <plNom default="ainmneacha" />
  <plGen default="ainmneacha" strength="strong" />
</noun>
"""


AINM_XML_HEADER = _HEADER + AINM_XML
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This script prepares LOTUS referenced structure-organism pairs \n,
   for further processing"""

import os

import pandas
import yaml

with open("paths.yaml", 'r') as stream:
    try:
        paths = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

os.chdir(paths["base_dir"])

col_list = [
    # 'structure_name',
    # 'structure_inchikey_2D',
    'structure_inchikey',
    'structure_smiles_2D',
    'structure_molecular_formula',
    'structure_exact_mass',
    # 'structure_xlogp',
    'structure_taxonomy_npclassifier_01pathway',
    'structure_taxonomy_npclassifier_02superclass',
    'structure_taxonomy_npclassifier_03class',
    'organism_name',
    'organism_taxonomy_01domain',
    'organism_taxonomy_02kingdom',
    'organism_taxonomy_03phylum',
    'organism_taxonomy_04class',
    'organism_taxonomy_05order',
    'organism_taxonomy_06family',
    'organism_taxonomy_07tribe',
    'organism_taxonomy_08genus',
    'organism_taxonomy_09species',
    'organism_taxonomy_10varietas',
    # 'reference_title',
    'reference_doi'
]

file_initial = pandas.read_csv(
    filepath_or_buffer=paths["data"]["source"]["libraries"]["lotus"],
    usecols=col_list
)

file_formatted = file_initial.assign(
    structure_inchikey_2D=file_initial.structure_inchikey.str[0:13]
).drop(
    columns='structure_inchikey'
).drop_duplicates()

file_formatted.to_csv(
    path_or_buf=paths["data"]["interim"]["libraries"]["lotus"]
)

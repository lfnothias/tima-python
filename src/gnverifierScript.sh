#!/usr/bin/env bash
# -*- coding: utf-8 -*-

source src/parse_yaml.sh
source src/warning_gnverifier.sh

eval $(parse_yaml src/paths.yaml)

${GNVERIFIER} $data_interim_taxa_original -s 3,4,5,6,8,9,11,12,118,128,132,147,148,150,155,158,163,164,165,167,169,174,175,179,180,187 -j 200 -f compact >$data_interim_taxa_verified
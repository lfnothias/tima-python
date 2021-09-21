#!/usr/bin/env bash
# -*- coding: utf-8 -*-
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
. "$SCRIPT_DIR"/parse_yaml.sh
. "$SCRIPT_DIR"/warning.sh

eval $(parse_yaml paths.yaml)

mkdir -p $data_source_libraries_path

wget "https://osf.io/rheq5/download" -O $data_source_libraries_lotus

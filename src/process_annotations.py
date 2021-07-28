#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You can use this script with the following example:
python process_annotations.py

Usage: process_annotations.py [--output=<output>] [--annotation=<annotation>] [--complement=<complement>] [--edges=<edges>] [--features=<features>][--initial.candidates=<initial.candidates>] [--k.top=<k.top>] [--library=<library>] [--ms=<ms>] [--name=<name>] [--ppm=<ppm>] [--rt=<rt>] [--force=<force>]

Options:
  -a --annotation=<annotation>  The file containing your prepared annotations
  -c --complement=<complement>  Logical: TRUE to complement with MS1 annotation, FALSE not to.
  -e --edges=<edges>            The file containing your prepared edges
  -f --features=<features>      The file containing your prepared features
  -i --initial.candidates=<initial.candidates>      Number of initial candidates to be considered.
  -k --k.top=<k.top>            Number of final candidates to be considered.
  -l --library=<library>        Library to be used.
  -m --ms=<ms>                  MS mode used ('pos' or 'neg')
  -n --name=<name>              Name given to the adducted library.
  -o --output=<output>          Filename for the output. Can be .gz.
  -p --ppm=<ppm>                Tolerance for MS1 annotation complement. Should not exceed 20 ppm.
  -r --rt=<rt>                  Tolerance for adduct attriubtion. Should not exceed 0.1 min.
  -h --help                     Show this screen.
  -v --version                  Show version.
  -0 --force=<force>            Logical: TRUE to force running with non-recommended parameters. Use it at yur own risks. Can crash. 

"""

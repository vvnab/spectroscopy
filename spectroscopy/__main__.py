#!/bin/python3

import argparse
import yaml
import csv
from .lib import Spectroscopy
from .argparser import parser

parser.add_argument('--input', type=argparse.FileType('r'),
                    help="путь к файлу входных данных {CSV}, по умолчанию stdin", default="-")
parser.add_argument('--output', type=argparse.FileType('w'),
                    help="путь к файлу для сохранения результата анализа, по умолчанию stdout", default="-")
parser.add_argument('--format', help="формат выходных данных, Markdown или Comma-separated values",
                    choices=["MD", "CSV"], default="MD")

args = parser.parse_args()

def main():
    for fileinput_line in args.input:
        if 'Exit' == fileinput_line.rstrip():
            break

        if args.output.name == '<stdout>':
            print(
                f'*****{fileinput_line}*****')
        else:
            args.output.write(fileinput_line)

    print("Done")


#!/bin/python3

import argparse
import yaml
import csv

parser = argparse.ArgumentParser(
    prog='spectroscopy',
    description='Определяет материал по линиям спектра',
    epilog='Набережный Евгений, Технический Лицей 2024 (c)')

parser.add_argument('--db', type=argparse.FileType('r'),
                    help="путь к файлу базы данных спектральных линий в формате YAML, ./db.yaml по умолчанию", default="db/db.yaml")
parser.add_argument('--input', type=argparse.FileType('r'),
                    help="путь к файлу входных данных {CSV}, по умолчанию stdin", default="-")
parser.add_argument('--output', type=argparse.FileType('w'),
                    help="путь к файлу для сохранения результата анализа, по умолчанию stdout", default="-")
parser.add_argument('--format', help="формат выходных данных, Markdown или Comma-separated values",
                    choices=["MD", "CSV"], default="MD")

args = parser.parse_args()
print(args.db, args.input, args.output, args.format)

for fileinput_line in args.input:
    if 'Exit' == fileinput_line.rstrip():
        break
    print(
        f'Processing Message from fileinput.input() *****{fileinput_line}*****')

print("Done")

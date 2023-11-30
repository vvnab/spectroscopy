import argparse

parser = argparse.ArgumentParser(
    prog='spectroscopy',
    description='Определяет материал по линиям спектра',
    epilog='Набережный Евгений, Технический Лицей 2024 (c)')

parser.add_argument('--db', type=argparse.FileType('r'),
                    help="путь к файлу базы данных спектральных линий в формате YAML, data/db.yaml по умолчанию", default="data/db.yaml")

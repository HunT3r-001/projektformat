import os
import argparse

parser = argparse.ArgumentParser(description='Opis programu')
parser.add_argument('x', help='plik wejsciowy')
parser.add_argument('y', help='plik wyjsciowy')

args = parser.parse_args()


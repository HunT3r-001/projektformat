import os
import argparse
import sys
import json

parser = argparse.ArgumentParser(description='Opis programu')
parser.add_argument('x', help='plik wejsciowy')
parser.add_argument('y', help='plik wyjsciowy')

args = parser.parse_args()

#odczytuje format pliku wejściowego
filename = args.x
extension = os.path.splitext(filename)[1]
#odczytuje format pliku wyjściowego
filename2 = args.y
extension2 = os.path.splitext(filename2)[1]



def mainf(ext):

    if ext=='.json':
        def jsonl(ex):



            #ścieżka do pliku JSON
            json_file=ex

            #wczytanie danych z pliku JSON i umieszczenie ich w zmiennej oraz sprawdzanie poprawności składni pliku json
            try:
                with open(json_file, 'r') as f:
                    data = json.load(f)

            except ValueError as e:
                print('Błąd składni JSON:', e)
                sys.exit()
            else:
                print('Plik json ma poprawną składnie')



            return
        jsonl(args.x)
    elif ext == '.xml':
        pass
    elif ext == '.yml':
        pass
    else:
        print('Podałeś złe formaty plików')
    return


mainf(extension)
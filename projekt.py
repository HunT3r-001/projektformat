import os
import argparse
import sys
import json
import xml.etree.ElementTree as ET
import yaml
import xmltodict

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
                print('Plik json ma poprawną składnie\n')
            if extension2=='.xml':
                # funkcja rekurencyjnie tworząca elementy XML na podstawie obiektu JSON
                def create_xml_element(key, value):
                    element = ET.Element(key)
                    if isinstance(value, dict):
                        for k, v in value.items():
                            element.append(create_xml_element(k, v))
                    else:
                        element.text = str(value)
                    return element

                # utworzenie węzła głównego XML na podstawie obiektu JSON
                root = ET.Element('root')
                for key, value in data.items():
                    root.append(create_xml_element(key, value))

                # utworzenie drzewa XML
                tree = ET.ElementTree(root)

                # zapisanie drzewa XML do pliku
                tree.write(args.y, encoding='utf-8', xml_declaration=True)
                print(f'Plik został poprawnie przeformatowany z {extension} na {extension2} i zapisany {args.y}')

            if extension2=='.yaml' or extension2=='.yml':

                # Konwertuj dane z formatu JSON na YAML
                yaml_data = yaml.dump(data)

                # Zapisz dane do pliku YAML
                with open(args.y, "w") as f:
                    f.write(yaml_data)
                    print(f'Plik został poprawnie przeformatowany z {extension} na {extension2} i zapisany {args.y}')

            return
        jsonl(args.x)

    elif ext == '.xml':
        def xmll(ex):
            # Otworzy plik XML, wczyta dane i sprawdzi poprawność składni pliku xml
            try:

                with open(ex, 'r') as f:
                    xml_str = f.read()
                    print('Plik xml ma poprawną składnie')

            except:
                print('Błąd składni pliku XML.')

            if extension2=='.json':

                # Konwertuj dane do formatu JSON
                json_data = json.dumps(xml_str)

                # Zapisujemy obiekt JSON do pliku
                with open(args.y, 'w') as f:
                    json.dump(json_data, f)
                    print(f'Plik został poprawnie przeformatowany z {extension} na {extension2} i zapisany {args.y}')

            if extension2=='.yml' or extension2=='.yaml':

                # Konwersja obiektu XML na słownik Pythona
                xml_dict = xmltodict.parse(xml_str)

                # Konwersja słownika Pythona na obiekt YAML i zapis do pliku YAML
                with open(args.y, 'w') as f:
                    yaml.dump(xml_dict, f)
                    print(f'Plik został poprawnie przeformatowany z {extension} na {extension2} i zapisany {args.y}')
            return
        xmll(args.x)

    elif ext == '.yml' or ext == '.yaml':
        def yml(ex):
            
            # Otwiera plik YAML i wczytuje dane oraz weryfikuje poprawność składni pliku yml
            with open(ex, "r") as f:
                try:
                    yaml_data = yaml.safe_load(f)
                    print("Plik YAML ma poprawną składnie")
                except yaml.YAMLError as e:
                    print("Błąd składni pliku YAML:", e)
                    sys.exit()

            if extension2=='.json':
                # Konwertuj dane YAML na JSON
                json_data = json.dumps(yaml_data)
                #zapisujemy dane json do pliku
                with open(args.y, "w") as f:
                    json.dump(json_data, f)
                    print(f'Plik został poprawnie przeformatowany z {extension} na {extension2} i zapisany {args.y}')

            if extension2=='.xml':
                # Funkcja pomocnicza do tworzenia elementów XML
                def create_element(name, text=None):
                    element = ET.Element(name)
                    element.text = text
                    return element

                # Funkcja pomocnicza do konwersji danych YAML na elementy XML
                def yaml_to_xml(yaml_data, parent=None):
                    if isinstance(yaml_data, dict):
                        if parent is None:
                            parent = ET.Element("root")
                        for key, value in yaml_data.items():
                            child = create_element(key)
                            parent.append(child)
                            yaml_to_xml(value, child)
                        return parent
                    elif isinstance(yaml_data, list):
                        for item in yaml_data:
                            yaml_to_xml(item, parent)
                    else:
                        text = str(yaml_data)
                        if parent is not None:
                            parent.text = text
                        return create_element("value", text)

                # Konwertuj dane YAML na elementy XML
                xml_data = yaml_to_xml(yaml_data)

                # Zapisz elementy XML do pliku
                with open(args.y, "wb") as f:
                    f.write(ET.tostring(xml_data))
                    print(f'Plik został poprawnie przeformatowany z {extension} na {extension2} i zapisany {args.y}')

            return
        yml(args.x)

    else:
        print('Podałeś złe formaty plików')
    return


mainf(extension)
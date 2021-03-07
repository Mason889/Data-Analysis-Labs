import xmltodict
import json

path = "/Users/install/Data-Analysis"                                  # your path

with open(f'{path}/lab01/final.xml', 'r', encoding='utf-8') as xml_file:
    data_dict=xmltodict.parse(xml_file.read())
    xml_file.close()
    with open(f'{path}/lab02/final.json', 'w', encoding='utf-8') as g:
        json.dump(data_dict, g, ensure_ascii=False)
        g.close()
import pandas_read_xml as pdx
import json

path = "/Users/install/Data-Analysis"                                  # your path

df = pdx.read_xml(f'{path}/lab01/final.xml', ['rss'])

with open(f'{path}/lab02/final.json', 'w', encoding='utf-8') as g:
    # json.dump(df.to_json(), g, ensure_ascii=False)
    g.write(df.to_json())
import pandas_read_xml as pdx

path = "/Users/install/Data-Analysis"                                  # your path

df = pdx.read_xml(f'{path}/lab01/final.xml')

with open(f'{path}/lab02/final.json', 'w', encoding='utf-8') as g:
    g.write(df.to_json())
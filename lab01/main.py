import os
import xml.etree.ElementTree as ET

path = "/Users/install/Data-Analysis"                                    # your path

final = ET.parse(f'{path}/lab01/final.xml')                              # final file with all rss data
finalroot = final.getroot()
finalinks = [item for item in finalroot[0].findall('item')]              # list of links

for (_, _, filenames) in os.walk(f'{path}/lab01/rss'):
    for filename in filenames:
        try:
            rss=ET.parse(f'{path}/lab01/rss/'+filename)
        except ParseError:
            print(f'ParseError in file {filename}: {ParseError}\n')
            continue

        rssroot = rss.getroot()
        for x in rssroot[0].findall('item'):
            link = x.find('link').text
            if link not in finalinks:
                finalinks.append(link)
                finalroot[0].append(x)

final.write(f'{path}/lab01/final.xml')
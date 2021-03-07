from urllib.parse import urlparse
import requests
import json
import datetime

path = "/Users/install/Data-Analysis"
ES_URL = "http://localhost:9200"

with open(f'{path}/lab02/final.json', 'r', encoding='utf-8') as rss_json:
    data = json.load(rss_json)
    rss_json.close()
    for element in data['rss']['channel']['item']:
        r = requests.post(url = f'{ES_URL}/daan/rss', json = {
            "title": f'{element["title"]}',
            "link": f'{element["link"]}',
            "source": f'{urlparse(element["link"]).hostname}',
            "description": f'{element["description"]}',
            "pubDate": f'{element["pubDate"]}' if 'pubDate' in element else f'{datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")}'
        })
        #print(f'RSS feed was successfully uploaded with _id={json.loads(r.text)["_id"]}')  # debug & visualize
        print(f'Some error with upload: {r.text}') if r.status_code != 201 else ''
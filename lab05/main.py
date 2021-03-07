from urllib.parse import urlparse
import requests
import json
import datetime

path = "/Users/install/Data-Analysis"
ES_URL = "http://localhost:9200"

with open(f'{path}/lab05/hb.json', 'r', encoding='utf-8') as rss_json:
    data = json.load(rss_json)
    rss_json.close()
    for element in data['items']:
        r = requests.post(url = f'{ES_URL}/dalw/rss-set', json = {
            "id": f'{element["id"]}',
            "title": f'{element["title"]}',
            "textBody": f'{element["textBody"]}',
            "source": f'{element["source"]}',
            "user": f'{element["user"]}',
            "pubDate": f'{element["pubDate"]}',
            "URL": f'{element["URL"]}'
        })
        # print(f'RSS feed was successfully uploaded with _id={json.loads(r.text)["_id"]}')  # debug & visualize
        print(f'Some error with upload: {r.text}') if r.status_code != 201 else ''
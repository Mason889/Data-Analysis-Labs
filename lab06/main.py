import requests
import json

ES_URL = 'http://localhost:9200'

r = requests.get(url = f'{ES_URL}/dalw/rss-set/_search?pretty=true', json = {
    "query": {
        "multi_match": {
            "query": "Samsung",
            "fields": ["title", "textBody"]
        }
    },
    "aggregations": {
        "dates_with_holes": {
            "date_histogram": {
                "field": "pubDate", 
                "interval": "day",
                "min_doc_count": 0
            }
        }
    }
})

if r.status_code == 200:
    data = json.loads(r.text)
    print(data)
    # print(f'<h3>Count of matched objects: {data["hits"]["total"]["value"]}</h3><hr><ol>')
    # for o in data["hits"]["hits"]:
    #     print(f'<li><b>Title:</b> {o["_source"]["title"]}')
    #     print(f'<br><b>Link:</b> {o["_source"]["link"]}')
    #     print(f'<br><b>Description:</b> {o["_source"]["description"]}')
    #     print(f'<br><b>Publication Date:</b> {o["_source"]["pubDate"]}<hr>')
else:
    print(f'Some error during code execution<br>Error log: {r.text}')
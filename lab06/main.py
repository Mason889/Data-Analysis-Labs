import requests
import json, csv

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
    with open('aggregation_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['key_as_string', 'doc_count']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')
        csvwriter.writeheader()
        for o in data["aggregations"]["dates_with_holes"]["buckets"]:
            csvwriter.writerow({'key_as_string': o['key_as_string'], 'doc_count': o['doc_count']})
        csvfile.close()
else:
    print(f'Some error during code execution<br>Error log: {r.text}')
#!/usr/bin/python3.8
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers
print('<head><meta charset="UTF-8"></head>')
print("<TITLE>CGI script output</TITLE>")
print("<h2>Output of your query</h2><br>")
import cgi, cgitb
import requests
import json

cgitb.enable()

ES_URL = 'http://elastic:9200'

form = cgi.FieldStorage()
query = form.getvalue('search_query')
source =  form.getvalue('seach_src')

r = requests.get(url = f'{ES_URL}/_all/_search?pretty=true&size=100', json = {
    "query": {
        "bool": {
            "must": [
                {
                    "multi_match": {
                        "query": str(query),
                        "fields": [
                            "description", "title"
                        ]
                    }
                }
            ],
            "filter": [
                {
                    "match": {
                        "source": str(source)
                    }
                }
            ]
        }
    }
})

if r.status_code == 200:
    data = json.loads(r.text)
    print(f'<h3>Count of matched objects: {data["hits"]["total"]["value"]}</h3><hr><ol>')
    for o in data["hits"]["hits"]:
        print(f'<li><b>Title:</b> {o["_source"]["title"]}')
        print(f'<br><b>Link:</b> {o["_source"]["link"]}')
        print(f'<br><b>Description:</b> {o["_source"]["description"]}')
        print(f'<br><b>Publication Date:</b> {o["_source"]["pubDate"]}<hr>')
    print("</ol>")
else:
    print(f'Some error during code execution<br>Error log: {r.text}')
# Data Analysis Labs
## Lab01
Requirements:
* Python 3.8.5
* Linux host
* Internet connection
## Lab02
Requirements:
* Python 3.8.5

Also use `pip install pandas-read-xml` before running `xml_convert.py` Python script.
## Lab03
Requirements:
* Docker
* pip packages: requests, datetime, json

Create Docker network:
`docker network create -d bridge elastic`

Docker run command for Elasticsearch: 
`docker run -d --network elastic --name elasticsearch --hostname elastic -p 9200:9200 -p 9300:9300 -e discovery.type=single-node docker.elastic.co/elasticsearch/elasticsearch:7.10.1`

## Lab04
Docker run command `docker run --network elastic -p 8883:80 -d --name httpd_cgi --hostname httpd_cgi httpd_cgi_python`
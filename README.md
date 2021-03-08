# Data Analysis Labs
## Lab01
Requirements:
* Python 3.8.5
* Linux host
* Internet connection
## Lab02
Requirements:
* Python 3.8.5

Also use `pip install xmltodict` before running `xml_convert.py` Python script.
## Lab03
Requirements:
* Docker
* pip packages: requests, datetime, json

Create Docker network:
`docker network create -d bridge elastic`

Docker run command for Elasticsearch: 
`docker run -d --network elastic --name elasticsearch --hostname elastic -p 9200:9200 -p 9300:9300 -e discovery.type=single-node docker.elastic.co/elasticsearch/elasticsearch:7.10.1`

## Lab04
Build Docker image httpd_cgi_python with needed files `docker build -t httpd_cgi_python -f Dockerfile .`
Docker run command `docker run --network elastic -p 8883:80 -d --name httpd_cgi --hostname httpd_cgi httpd_cgi_python`

## Lab05
Before running of python command, you need to run elasticseach & kibana in docker
Docker run for kibana: `docker run -d --network elastic --name kibana --hostname kibana -p 5601:5601 -e ELASTICSEARCH_URL=http://elastic:9200 -e ELASTICSEARCH_HOSTS=http://elastic:9200 docker.elastic.co/kibana/kibana:7.10.1`
Run python command `python main.py` for data migration from file hb.json
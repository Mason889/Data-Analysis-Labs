#!/bin/bash

urls=(
    https://habr.com/ru/rss/all/all/?fl=ru 
    https://3dnews.ru/news/rss/ 
    https://techtoday.in.ua/feed 
    https://pcnews.ru/feeds/latest/news/ 
    https://pcnews.ru/feeds/latest/articles/
    https://ko.com.ua/rss.xml/
    https://ko.com.ua/rss/article
    https://www.helpnetsecurity.com/feed/
    https://www.itweek.ru/rss/
    http://ipt.kpi.ua/feed
    http://www.fpm.kpi.ua/rss.xml
)

shortnames=(
    habr 
    3dnews
    techtoday 
    pcnews-news 
    pcnews-articles 
    ko 
    ko-article 
    helpnetsecurity
    itweek
    ipt
    fpm
)

for item in ${!urls[*]}
do
    curl ${urls[$item]} --output $(pwd)/rss/$(date +"%F")-${shortnames[$item]}.xml
done
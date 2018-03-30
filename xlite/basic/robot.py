# IT之家
rsslist = ['https://www.ithome.com/rss/', ]

# coding=UTF-8

import re
import os
import sys
import bleach
import django
import requests
from bs4 import BeautifulSoup
headers =  {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}

pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, pathname)
sys.path.insert(0, os.path.abspath(os.path.join(pathname, '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xlite.settings")
django.setup()
from basic.models import Articles

def getArticles(url):
    HTML = requests.get(url, headers)
    HTML.encoding = 'UTF-8'
    SOUP = BeautifulSoup(HTML.text, 'lxml')
    items = SOUP.find_all('item')
    for item in items:
        title = item.find('title').text
        if  Articles.objects.filter(title=title):
            continue
        else:
            body = bleach.linkify(str(item.find('description')))
            body = re.sub(r'(<description>)|(</description>)|(]]&gt;\n)', '', body)[25:]
            cover = re.findall(r'<img.*src="(.*?)"', body, re.I)
            if cover:
                cover = cover[0]
            else:
                cover = '/static/baisc/img/1.jpg'
            try:
                Articles(title=title,body=body,cover=cover).save()
            except:
                continue

def main():
    for rss in rsslist:
        getArticles(url=rss)
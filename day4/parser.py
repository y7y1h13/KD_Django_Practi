from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
#장고 접근 가능

from post.models import Category


def parse_post():
    baseUrl = 'https://www.youtube.com/results?search_query='
    plusUrl = input('search :')

    url = baseUrl + quote_plus(plusUrl)

    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    lists = soup.select('#video-title')
    data = {}
    for list in lists:
        print(list.get('title') + list.get('href'))
        data[list.text] = list.get('href')

    driver.close()

    return data

if __name__ == '__main__':
    post_data = parse_post()
    for title, hr in post_data.items():
        Category(name=title, slug=hr).save()
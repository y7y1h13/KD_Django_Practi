from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.parse import quote_plus #한글 처리를 위해서
import time


# baseUrl = 'https://www.google.com/search?q='
baseUrl = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query='
plusUrl = input('검색어를 입력하세요. : ')


url = baseUrl + quote_plus(plusUrl)#quote_plus 꼭 써야함

print(url)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser') #html을 잘게잘라서 담겠다

f = open("a_text.txt", 'w')


# titleLists = soup.select('h3')

#
# for title in titleLists:
#     data = title.text + "\n"
#     f.write(data)

titleLists = soup.select('.api_txt_lines')
for title in titleLists:
    print(title.text)
    print(title.get('href'))


f.close()

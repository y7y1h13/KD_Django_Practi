from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')

time.sleep(0.5)
e = driver.find_elements_by_class_name('_2hvTZ')[0]
#e.click() autofocus없으면 이거 써야함
e.send_keys('01092738022')

e = driver.find_elements_by_class_name('_2hvTZ')[1]
e.send_keys('dbgusals12!')

e.send_keys(Keys.ENTER)#키 입력

time.sleep(3)
e = driver.find_elements_by_class_name('sqdOP')[1]
e.click()
time.sleep(1)
e = driver.find_elements_by_class_name('aOOlW')[1]
e.click()

# e = driver.find_elements_by_class_name('Ypffh')[0]
# e.click()
# e = driver.find_elements_by_class_name('Ypffh')[0]
# e.send_keys("가")
# e.send_keys(Keys.ENTER)

#댓글 가져오기
e = driver.find_elements_by_class_name('QzzMF')[0].text
print(e)
#사진 가져오기
e = driver.find_elements_by_class_name('FFVAD')[0].get_attribute('src')
print(e)
import os

import bs4
import html5lib
import selenium;import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t

url='https://bitcointicker.co/'
opts=selenium.webdriver.firefox.options.Options()
driver = webdriver.Firefox()
driver.get(url)
temp_val=[0]
for i in range(0,100):
	t.sleep(1)
	heading1 = driver.find_element('lastTrade').text
	temp_val.append(heading1)
	if temp_val[1]==temp_val[0]:
		pass
	else:
		print(temp_val[1])
	temp_val.pop(0) #because We using FIFO data structure

driver.close()

'git appended changes'


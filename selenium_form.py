from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import json

client = MongoClient("ds239359.mlab.com", 39359, connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True)

db = client["wolfpal"]
db.authenticate("paylot","wolfpal123")

url = 'https://www.acs.ncsu.edu/php/coursecat/directory.php'

driver = webdriver.Chrome()

driver.get(url)



driver.find_element_by_xpath("//select[@name='course-career']/option[text()='Graduate']").click()

code = driver.find_element_by_id("auto-subject")
code.send_keys("CSC")
#code.send_keys(Keys.DOWN)
#code.send_keys(Keys.ENTER)

driver.find_element_by_id("subject-search-button").click()

time.sleep(10)

print driver.current_url
page = requests.get(driver.current_url)

#print page.text
#durlsoup = BeautifulSoup(page.text,"html.parser")


html_list = driver.find_element_by_id("course-search-results")
items = html_list.find_elements_by_tag_name("li")
# list_of_courses = []
# fp = open("CSC-course-list.txt","w")
# for item in items:
#     text = item.text
#     fp.write(text)
#     fp.write('\n')
# fp.close()
description = []
unit = []
title = []
# for item in items:
# 	print item.text
for item in items:
	print item.text
	driver.find_element_by_link_text(item.text).click()
	time.sleep(5)
	description.append(driver.find_element_by_id("course-descr").text)
	print description
	unit.append(driver.find_element_by_id("course-units").text)
	print unit
	title.append(driver.find_element_by_id("modalTitle").text)
	print title
	time.sleep(5)
	driver.find_element_by_xpath("//*[contains(text(), 'Close')]").click()
	time.sleep(5)

#button.click()

#print urlsoup.prettify()
# print urlsoup

# description = urlsoup.find("p",id="course-descr").text

# print description
print description



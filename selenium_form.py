from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests


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
driver.find_element_by_link_text("CSC 506 - Architecture Of Parallel Computers").click()

print driver.current_url
page = requests.get(driver.current_url)
#print page.text
#durlsoup = BeautifulSoup(page.text,"html.parser")

description = driver.find_element_by_id("course-descr").text
unit = driver.find_element_by_id("course-units").text
title = driver.find_element_by_id("modalTitle")
#print urlsoup.prettify()
# print urlsoup

# description = urlsoup.find("p",id="course-descr").text

# print description
print description

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import json
import  script_db
import pickle

# def get_credentials():
#     pkl_file = open('.cred.pkl', 'rb')
#     data = pickle.load(pkl_file)
#     return data[0], data[1], data[2], data[3]

# username, password, db_name, collection_name = get_credentials()

# client = MongoClient("ds239359.mlab.com", 39359, connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True)

# db = client["wolfpal"]
# db.authenticate("paylot","wolfpal123")

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
prereqs = []
#days = []
descriptions = []
unit = []
title = []
names = []
ids = []
timings = []
schedule = []
courses = []
i = 1
# for item in items:
# 	print item.text
for item in items:
	days = []
	print item.text
	driver.find_element_by_link_text(item.text).click()
	time.sleep(10)
	description = (driver.find_element_by_id("course-descr").text)
	descriptions.append(description)
	unit.append(driver.find_element_by_id("course-units").text)
	print unit
	prereq = driver.find_element_by_id("course-reqs").text
	prereqs.append(prereq)
	print prereqs
	t = driver.find_element_by_id("modalTitle").text
	print t
	id_name = t.split(":")
	id_name[0] = id_name[0].replace(" ","")
	id_name[1]= id_name[1].lstrip()
	title.append(driver.find_element_by_id("modalTitle").text)
	print title
	ids.append(id_name[0])
	names.append(id_name[1])
	print ids
	print names
	sem = driver.find_element_by_tag_name("em").text
	if "Fall" and "Spring" in sem:
		semester = "Fall,Spring"
	elif "Fall" in sem:
		semester = "Fall"
	elif "Spring" in sem:
		semester = "Spring"
	print semester
	if " future" in driver.find_element_by_id("course-sem").text:
		days.append("NA")
	else:	
		term = driver.find_element_by_partial_link_text("2018").click()
		time.sleep(10)
		dayl = driver.find_elements_by_css_selector('li.meet.hidden-xs')
		for day in dayl:
			days.append(day.text)
		timing = driver.find_element_by_xpath("""//*[@id="search-results"]/table/tbody/tr/td[5]""").text.split('\n')
		if "TBD" not in timing:
			timeslot = timing[1]
		else:
			timeslot = "TBD"
	print days
	print timeslot
	#script_db.db_insert(username,password,db_name,collection_name,id_name[0],id_name[1],"Fall",description)
	driver.find_element_by_xpath("""//*[@id="details-modal"]/div/div/div[3]/button""").click()
	time.sleep(10)
	

	json_schedule = json.dumps(
		{
		'course_id': i,
		'semester': semester,
		'day':days,
		'time':timeslot,
		'project': True,
		'fieldwork': True,
		'ratings': 4

		})
	entry_s = json.loads(json_schedule)

	schedule.append(entry_s)
	#print schedule

	json_courses = json.dumps(
		{
		'code': id_name[0],
		'syllabus_id': i,
		'course_name': id_name[1],
		'description':description,
		'core': True,
		'channel_id': i,
		})
	entry_c = json.loads(json_courses)

	courses.append(entry_c)
	#print courses
	i = i+1

	fp1 = open("courses.txt","w")
	fp1.write(str(courses))
	fp1.close()

	fp2 = open("schedule.txt","w")
	fp2.write(str(schedule))
	fp2.close()

#button.click()

#print urlsoup.prettify()
# print urlsoup

# description = urlsoup.find("p",id="course-descr").text

# print description
#print description





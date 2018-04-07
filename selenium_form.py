from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.acs.ncsu.edu/php/coursecat/directory.php'

driver = webdriver.Chrome()

driver.get(url)

driver.find_element_by_xpath("//select[@name='course-career']/option[text()='Graduate']").click()

code = driver.find_element_by_id("auto-subject")
code.send_keys("CSC")
#code.send_keys(Keys.DOWN)
#code.send_keys(Keys.ENTER)

driver.find_element_by_id("subject-search-button").click()

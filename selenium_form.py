from selenium import webdriver
url = 'https://www.acs.ncsu.edu/php/coursecat/directory.php'

driver = webdriver.Chrome()

driver.get(url)

driver.find_element_by_xpath("//select[@name='course-career']/option[text()='Graduate']").click()
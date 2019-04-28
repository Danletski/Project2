#SitePrinter
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

#Driver location
driver = webdriver.Chrome(executable_path='/Users/dans/Documents/Devops/chromedriver')

#Open website
driver.get('http://192.168.99.100:5000')


#Wait for page to load
driver.implicitly_wait(3)

#Locate text
html = driver.page_source
print(html)

#Close page
driver.close()

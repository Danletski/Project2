#SitePrinter
from selenium import webdriver

#Driver location
driver = webdriver.Chrome(executable_path='/Users/dans/Documents/GitHub/Project2/chromedriver')

#Open website
driver.get('http://192.168.99.100:5000')


#Wait for page to load
driver.implicitly_wait(3)

#Locate text
#html = driver.page_source
print('123')

#Close page
driver.close()

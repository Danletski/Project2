#SitePrinter
from selenium import webdriver

#Driver location
driver = webdriver.Chrome(executable_path='/Users/dans/Documents/Devops/chromedriver')

#Open website (Docker IP).
driver.get('http://192.168.99.100:5000')


#Wait for page to load
driver.implicitly_wait(3)

#Locate text
html = driver.find_element_by_xpath('//html/body')
    #driver.find_elements_by_css_selector('textarea')[0]

print(html.text)

#Close page
driver.close()

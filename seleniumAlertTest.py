from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

import time

chrome_options=Options()
#chrome_options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver=webdriver.Chrome(chromedriver,options=chrome_options)
driver.get("http://127.0.0.1:8081")

obj = driver.switch_to.alert

time.sleep(2)

obj.send_keys('Hello MK, How are you today')

obj.accept()

# inputElement = driver.find_element_by_name("q")
# inputElement.send_keys("Hello google")
# inputElement.submit()

#link = driver.find_element_by_css_selector("table.table.params")

#link = driver.find_elements_by_xpath("//table/tbody/tr/td[contains(text(),'https')]")

#print(link[0].text)


time.sleep(10)
#driver.close()
driver.quit()
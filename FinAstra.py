from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
# driver.maximize_window()
wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located


driver.get("http://xtreme:8000/Login/Index")

def FinAstra_login():
    driver.find_element_by_xpath("//*[@id='UserName']").send_keys("office")
    driver.find_element_by_xpath("//*[@id='UserPassword']").send_keys("1<2.1")
    driver.find_element_by_xpath("//*[@id='login']").click()

FinAstra_login()

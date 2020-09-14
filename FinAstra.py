from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
# import selenium-requests

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.maximize_window()
driver.maximize_window()
wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located
port = driver.get("http://xtreme:8000/")

def FinAstra_login():
    driver.find_element_by_xpath("//*[@id='UserName']").send_keys("**")
    driver.find_element_by_xpath("//*[@id='UserPassword']").send_keys("**")
    driver.find_element_by_xpath("//*[@id='login']").click()

FinAstra_login()

def Share_purchase():
    time.sleep(2)
    driver.get("http://xtreme:8000/Member/BankShare/SharePurchase")
    driver.find_element_by_xpath("//*[@id='MemberNo_chosen']").click()
    driver.find_element_by_xpath("//*[@id='MemberNo_chosen']/div/div/input").send_keys("M00001")
    driver.find_element_by_xpath("//*[@id='MemberNo_chosen']/div/ul/li").click()
    driver.find_element_by_xpath("//*[@id='ShareNo']").send_keys("10")
    driver.find_element_by_xpath("//*[@id='MembershipFee']").send_keys("120.5")
    driver.find_element_by_xpath("//*[@id='Remarks']").send_keys("Share Remarks Test by Auto bot")
    driver.find_element_by_xpath("//*[@id='sharePurchase']/div/div/div/div[1]/div[6]/div/div/div/button").click()
    time.sleep(3)
    alert = driver.switch_to_alert()
    alert.accept()

Share_purchase()

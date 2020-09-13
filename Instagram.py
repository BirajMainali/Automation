from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver=webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located


driver.get("https://www.instagram.com/explore/people/suggested/")


def Instagram_Login():
    os.system("cls")
    UserName = input("Instagram UserName or Phone : ")
    UserPass = input("Instagram PassWord : ")
    os.system("cls")
    driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(UserName)
    driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(UserPass)
    driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()

Instagram_Login()

def ByPass_Login_Info():
    time.sleep(10)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()

ByPass_Login_Info()

def Anymonious_Follow():
    time.sleep(10)
    People=['1','2','3','5','6','8','9','10','11']
    for xx in People:
        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[2]/div/div/div["+str(xx)+"]/div[3]/button").click()
Anymonious_Follow()
# //Anymonious_Bot




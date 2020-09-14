from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.maximize_window()
driver.maximize_window()
wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

class FinAstra_Bot:

        def __init__(self):
            self.UserName = 'office'
            self.Password = '1<2.1'
            self.MemberNo = 'M00001'
            self.ShareNo = '10'
            self.Fees = '290'
            self.Remarks ='Share Remarks Test by Auto bot'
            self.port = "http://xtreme:8000/"
            self.pruchase = "Member/BankShare/SharePurchase"
            self.Share_Performance_link = "Member/ShareReport/TotalSharePurchasedReport"
            self.Share_revert_link = "Member/TransactionEdit/SearchTransaction"

        def FinAstra_login(self):
            port = driver.get(str(self.port))
            driver.find_element_by_xpath("//*[@id='UserName']").send_keys(self.UserName)
            driver.find_element_by_xpath("//*[@id='UserPassword']").send_keys(self.Password)
            driver.find_element_by_xpath("//*[@id='login']").click()

        def Share_purchase(self):
            time.sleep(2)
            driver.get(str(self.port)+str(self.pruchase))
            driver.find_element_by_xpath("//*[@id='MemberNo_chosen']").click()
            driver.find_element_by_xpath("//*[@id='MemberNo_chosen']/div/div/input").send_keys(self.MemberNo)
            driver.find_element_by_xpath("//*[@id='MemberNo_chosen']/div/ul/li").click()
            driver.find_element_by_xpath("//*[@id='ShareNo']").send_keys(self.ShareNo)
            driver.find_element_by_xpath("//*[@id='MembershipFee']").send_keys(self.Fees)
            driver.find_element_by_xpath("//*[@id='Remarks']").send_keys(self.Remarks)
            driver.find_element_by_xpath("//*[@id='sharePurchase']/div/div/div/div[1]/div[6]/div/div/div/button").click()
            time.sleep(1.5)
            alert = driver.switch_to_alert()
            alert.accept()

        def Report_Performace(self):
            time.sleep(2)
            driver.get(str(self.port)+str(self.Share_Performance_link))

        def Share_Reverse(self):
            time.sleep(1.5)
            driver.get(str(self.port)+str(self.Share_revert_link))
            driver.find_element_by_xpath("//*[@id='SearchForm']/div[5]/button").click()
            driver.execute_script("window.scrollTo(0, 1000);")
            driver.execute_script("$('.selectcheckbox').click()")
            time.sleep(0.5)
            driver.find_element_by_xpath("//*[@id='ReverseForm']/div[3]/button").click()
            prompt = driver.switch_to_alert()
            prompt.send_keys("Share reverse")
            time.sleep(2)
            prompt.accept()


LG = FinAstra_Bot()
LG.FinAstra_login()
SP = FinAstra_Bot()
SP.Share_purchase()
RP = FinAstra_Bot()
RP.Report_Performace()
SR = FinAstra_Bot()
SR.Share_Reverse()
RP.Report_Performace()

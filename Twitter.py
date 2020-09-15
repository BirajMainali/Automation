from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Twitter_bot:

    def __init__(self,UserName,Password):
        self.UserName = UserName
        self.Password = Password
        self.bot = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login")
        time.sleep(2)
        Email = bot.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")
        Email.clear()
        Auth = bot.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")
        Auth.clear()
        Email.send_keys(self.UserName)
        Auth.send_keys(self.Password)
        Auth.send_keys(Keys.RETURN)
        time.sleep(2)

    def Like_Tweet(self,Hashtag):
        bot = self.bot
        bot.get("https://twitter.com/search?q=%23"+str(Hashtag)+"&src=typed_query")
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name("tweet")
            links = [el.get_attribute('data-permalink-path')
                    for el in tweets]
            for link in links:
                bot.get('https://twitter.com'+link)
                try:
                    bot.find_elements_by_class_name("r-1niwhzg").click()
                    time.sleep(7)
                except Exception as ex:
                    time.sleep(60)

Tw = Twitter_bot("9880687994","incorrect1530")
Tw.login()
Tw.Like_Tweet('Webdevelopment')

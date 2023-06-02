from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_drive_path = "C:\Development\chromedriver.exe"

username = "eitan.brochstein@icloud.com"
passwrd = "25Greenseed"

class HalloPalMessenger:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        time.sleep(1)
        self.driver.get("https://www.hallopal.com/login")
        email = self.driver.find_element(By.ID, "username")
        email.send_keys(username)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(passwrd)
        password.send_keys(Keys.ENTER)
        
    def action(self):
        buttons = self.driver.find_elements(By.CLASS_NAME, "btn-sm")
        for i in buttons:
            if i.text != "New":
                i.click()
                launchBtns = self.driver.find_elements(By.CLASS_NAME, "dropdown-item")
                for i in launchBtns:
                    if i.text == "Launch":
                        i.click()
        while True: pass

bot = HalloPalMessenger(chrome_drive_path)
bot.login()
bot.action()
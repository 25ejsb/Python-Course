from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_drive_path = "C:\Development\chromedriver.exe"
simillar_account = input("Enter an account you would like to target: ")
username = "25ejsb"
password = "25Greenseed"
import time
class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)
    
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login")
        time.sleep(1)
        user = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        user.send_keys(username)
        passwordinp = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        passwordinp.send_keys(password)
        passwordinp.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{simillar_account}/followers")
        time.sleep(2)
        modal = self.driver.find_element(By.CLASS_NAME, "_aano")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        buttons = self.driver.find_elements(By.CLASS_NAME, "_aj1-")
        for i in buttons:
            self.driver.execute_script("arguments[0].click()", i)
        while True: pass

bot = InstaFollower(chrome_drive_path)
bot.login()
bot.find_followers()
bot.follow()
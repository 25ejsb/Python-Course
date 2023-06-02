from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random
chrome_drive_path = "C:\Development\chromedriver.exe"
password = "YesSire999"
username = "PythonBotish"
complaints = ["Why Is Roblox Bedwars So Laggy?", "Why I am still here?", "Why Do People Think I'm Stupid?"]

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_drive_path)
        self.driver.get("https://twitter.com/login")
        time.sleep(1)
        self.newInput = self.driver.find_element(By.CSS_SELECTOR, "input")
        self.newInput.send_keys(username)
        self.newInput.send_keys(Keys.ENTER)
        time.sleep(1)
        self.password = self.driver.find_element(By.NAME, "password")
        self.password.send_keys(password)
        self.password.send_keys(Keys.ENTER)
        time.sleep(5)
        while True:
            self.tweet = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-ltr")
            self.tweet.send_keys(random.choice(complaints))
            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()
            time.sleep(3)

NewClass = InternetSpeedTwitterBot()
url = "https://www.zillow.com/homes/recently_sold/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-70.91708642114259%2C%22east%22%3A-70.78216057885743%2C%22south%22%3A42.46635518926465%2C%22north%22%3A42.54367837701337%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22min%22%3A300000%7D%2C%22mp%22%3A%7B%22min%22%3A1473%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22pagination%22%3A%7B%7D%7D"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, requests
from bs4 import BeautifulSoup
chrome_drive_path = "C:\Development\chromedriver.exe"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

result = requests.get(url, headers=header)

soup = BeautifulSoup(result.text, "html.parser")
prices = soup.select(selector=".bqsBln span")
address = soup.select(selector="address")

driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get("https://docs.google.com/forms/d/1ETIXIhXI2APmpGW7K5X_Af-5hW6ALgW5UblqAfWqzdA/edit")
time.sleep(1)
for i in range(len(prices)):
    time.sleep(1)
    ques1 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ques2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    ques1.send_keys(address[i].text)
    ques2.send_keys(prices[i].text)
    driver.execute_script("arguments[0].click()", submit)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
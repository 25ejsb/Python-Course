from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_drive_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# clicking
article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print("Article Count: " + article_count.text)
# article_count.click()

# Inputting
search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)

while True: pass
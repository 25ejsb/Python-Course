from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
chrome_drive_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get("https://cpstest.org")

buttontoclick = driver.find_element(By.ID, "start")
while True:
    driver.execute_script("arguments[0].click()", buttontoclick)
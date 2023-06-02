from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
chrome_drive_path = "C:\Development\chromedriver.exe"
import time

phone_number = "7812289821"

linked_in = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get(linked_in)

signin = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
signin.click()

username = driver.find_element(By.ID, "username")
username.send_keys("eitantravels25@gmail.com")

password = driver.find_element(By.ID, "password")
password.send_keys("25Greenseed")

signinbtn = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
signinbtn.click()

time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    try:
        time.sleep(2)
        applybtn = driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button')
        driver.execute_script("arguments[0].click()", applybtn)

        time.sleep(5)
        phone = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
        phone.send_keys(phone_number)

        nextbtn = driver.find_element(By.CSS_SELECTOR, "footer .ph5 button")
        nextbtn.click()
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
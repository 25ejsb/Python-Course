from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_drive_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get("https://www.python.org")

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li time")
names = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li a")
new_dict = {}
for i in range(len(dates)):
    add_dict = {"date": dates[i].text, "name": names[i].text}
    new_dict[i] = add_dict
print(new_dict)
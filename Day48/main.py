# stackoverflow on https://stackoverflow.com/questions/47508518/google-chrome-closes-immediately-after-being-launched-with-selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_drive_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_drive_path)
# driver.get("https://www.amazon.com/SkyTech-Chronos-Gaming-Computer-Desktop/dp/B09JBQN8P5/ref=sxin_16_ci_mcx_mi_sr_m_ts?content-id=amzn1.sym.5aa38d01-f4e4-49d0-aaaa-bf65d3f91314%3Aamzn1.sym.5aa38d01-f4e4-49d0-aaaa-bf65d3f91314&crid=37PFR27ODGHJO&cv_ct_cx=gaming%2Bcomputer&keywords=gaming%2Bcomputer&pd_rd_i=B09JBQN8P5&pd_rd_r=379a87a7-a483-4161-92f7-cfc329af8478&pd_rd_w=ES3cI&pd_rd_wg=VCXt1&pf_rd_p=5aa38d01-f4e4-49d0-aaaa-bf65d3f91314&pf_rd_r=X7F49TWHP891SAES26WR&qid=1680136562&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=%2Caps%2C126&sr=1-1-adf8a58d-854e-4c79-9f56-e84cb8dfa902&th=1")
# tagprice = driver.find_element(By.ID, "twotabsearchtextbox")
# print(tagprice.get_attribute("placeholder"))

driver.get("https://www.python.org")
# singular elements
logo = driver.find_element(By.CLASS_NAME, "python-logo")
# find element from the nearest class with css selector
docslink = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# xpath, get xpath by right clicking element -> Copy -> Copy XPATH
bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(f"{bug_link.text}\n{docslink.text}\n{logo.size}")

driver.quit()
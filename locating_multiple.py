from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"

driver.get(f"https://www.amazon.in/s?k={query}&crid=2FKHFKIW2WNUN&sprefix={query}%2Caps%2C239&ref=nb_sb_noss_2")
elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
print(f"{len(elems)} items found")
print(elems)

for elem in elems:
   print(elem.text)
#print(elem.get_attribute("outerHTML"))
#print(elem.text)

time.sleep(10)


driver.close()
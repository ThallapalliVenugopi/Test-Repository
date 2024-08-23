from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_obj = webdriver.Chrome()
driver_obj.get("https://www.saucedemo.com/")
driver_obj.maximize_window()
"this is by using id"
driver_obj.find_element(By.ID, "user-name").send_keys('standard_user')
"this is by using name"
driver_obj.find_element(By.NAME, "password").send_keys('secret_sauce')
"this is a XPATH"
driver_obj.find_element(By.XPATH, "//input[@ID='login-button']").click()
time.sleep(5)
"this is also id"
driver_obj.find_element(By.ID, 'react-burger-menu-btn').click()
time.sleep(2)
"this is a partialy link text"
#driver_obj.find_element(By.LINK_TEXT,'About').click()
#time.sleep(2)
driver_obj.find_element(By.PARTIAL_LINK_TEXTLINK_TEXTgit).click()
time.sleep(2)

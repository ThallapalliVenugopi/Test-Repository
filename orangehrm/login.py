import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from url import test_url
from locators import test_xpaths
from data import datas


def logins(urls=test_url.orange_hrm_url, usernames=datas.username, passwords=datas.password):
    driver = webdriver.Chrome()
    driver.get(urls)
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.NAME, test_xpaths.user_name_xpath).send_keys(usernames)
    driver.find_element(By.NAME, test_xpaths.password_xpath).send_keys(passwords)
    driver.find_element(By.XPATH, test_xpaths.click_button).click()
    print("Login successful")
    driver.quit()

logins()
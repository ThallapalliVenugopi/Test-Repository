from selenium import webdriver
from selenium.webdriver.common.by import By
from url import test_url
from data import datas
from orangehrm.login import logins
from locators import test_xpaths
import time


def negative(url=test_url.orange_hrm_url, username=datas.password, password=datas.username):
    driver = logins(url, username, password)
    time.sleep(5)
    error_message = driver.find_element(By.XPATH, test_xpaths.error_message_xpath).text
    assert error_message == datas.invalid_message
    return driver

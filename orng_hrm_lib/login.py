from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from test_data import data, urls
from locators import xpaths


def login_to_orange_hrm(url=urls.orange_hrm_url, username=data.username, password=data.password, browser='chrome'):

    if browser.lower() == 'chrome':
        driver_obj = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver_obj = webdriver.Firefox()
    elif browser.lower() == 'edge':
        driver_obj = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver_obj.get(url)
    driver_obj.maximize_window()
    "this is by using id"
    driver_obj.find_element(By.ID, xpaths.user_name_input_xpath).send_keys(username)
    "this is by using name"
    driver_obj.find_element(By.NAME, xpaths.password_input_xpath).send_keys(password)
    "this is a XPATH"
    driver_obj.find_element(By.XPATH, xpaths.login_button_xpath).click()
    time.sleep(5)
    "this is also id"
    driver_obj.find_element(By.ID, xpaths.burger_menu_button_xpath).click()
    time.sleep(2)
#%%
import pandas as pd
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import json
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

def init_crawler(url, driver=None):
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")

    if driver != None:
        driver.close()

    chrome_driver = ChromeDriverManager().install()
    service = Service(chrome_driver)
    new_driver = webdriver.Chrome(service=service, options=options)

    time.sleep(1)
    new_driver.get(url)
    return new_driver

def remove_blink(text):
    if " " in text:
        return "".join(text.split())
    else:
        return text

def close_current_tab(driver):
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    
def click_component(driver, selector):
    tmp = driver.find_element(By.CSS_SELECTOR, selector)
    tmp.click()

def send_key(driver, selector, key):
    tmp = driver.find_element(By.CSS_SELECTOR, selector)
    tmp.send_keys(key)
    
load_dotenv(verbose=True)
id = os.getenv("ID")
pw = os.getenv("PW")

login_url = (
    "https://accounts.kakao.com/login/kakaomap?continue=https%3A%2F%2Fmap.kakao.com"
)
url = "https://map.kakao.com/"

driver = init_crawler(login_url)
driver.implicitly_wait(1)

send_key(driver, "input#id_email_2", id)
send_key(driver, "input#id_password_3", pw)

click_component(driver, "form#login-form div.wrap_btn > button.btn_confirm.submit.btn_g")
click_component(driver, "div#dimmedLayer")
click_component(driver, "a.link_myfavorite")

folders = driver.find_elements(By.CSS_SELECTOR, "ul.list_detail a.link_txt")

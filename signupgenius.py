import time
import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


file_in = open("credentials.txt", "r")
usr = file_in.readline()
pwd = file_in.readline()

driver = webdriver.Chrome(executable_path='/Users/snagaraj/Downloads/chromedriver')
driver.get("https://www.signupgenius.com/register")

time.sleep(5)


password_box = driver.find_element_by_id("pword")
username_box = driver.find_element_by_id("email")
password_box.send_keys(pwd)
close_button = driver.find_element_by_class_name("mfp-close")
close_button.click()
time.sleep(3)
username_box.send_keys(usr)

time.sleep(3)


driver.get("https://www.signupgenius.com/go/8050845a8ae2fabf85-test")

time.sleep(5)	# Replace with Selenium waits

privacy_button = driver.find_element_by_class_name("sug-notice--privacy-button")
privacy_button.click();
time.sleep(5)
wait = WebDriverWait(driver, 10)

clickbox = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[id*="checkbox"]')))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
ActionChains(driver).move_to_element(clickbox).click(clickbox).perform()
clickbox.send_keys('\n')

time.sleep(10)

time.sleep(5)
submit_button = driver.find_element_by_xpath("//button[contains(.,'Sign Up Now')]")
submit_button.click()


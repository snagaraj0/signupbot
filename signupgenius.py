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

driver = webdriver.Chrome()
driver.get("https://www.signupgenius.com/register")

time.sleep(5)

#cookies_button = driver.find_element_by_class_name("sug-notice--privacy-button-wrapper")
#cookies_button.click()


password_box = driver.find_element_by_id("pword")
#password_box.send_keys(pwd)
username_box = driver.find_element_by_id("email")
password_box.send_keys(pwd)
close_button = driver.find_element_by_class_name("mfp-close")
close_button.click()
time.sleep(3)
username_box.send_keys(usr)

time.sleep(3)


#driver = webdriver.Chrome()
#driver.get("PUT LINK HERE")  UNCOMMENT THIS

time.sleep(5)	# Replace with Selenium waits

privacy_button = driver.find_element_by_class_name("sug-notice--privacy-button")
privacy_button.click();
time.sleep(5)
wait = WebDriverWait(driver, 10)

#WebElement inputt = driver.findElement(By.cssSelector('div.formfield input.siid'))
#WebElement input = driver.findElement(By.cssSelector('div.formfield input.siid'))
clickbox = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[id*="checkbox"]')))
#time.sleep(3)
#clickbox = driver.find_elements_by_css_selector("input[id*=siid]")
#print(clickbox)
#time.sleep(3)
ActionChains(driver).move_to_element(clickbox).perform()
time.sleep(3)
ActionChains(driver).click()
#time.sleep(3)
#clickbox = driver.find_element_by_id("checkbox699578695")
#driver.findElement(By.xpath("//span[contains(text(),"Sign Up")]")).click();
clickbox.send_keys('\n')

time.sleep(10)
#username_box = driver.find_element_by_id('firstname')
#username_box = driver.find_element_by_class_name("form-control ng-valid ng-valid-maxlength ng-not-empty ng-dirty ng-valid-parse ng-touched")
#username_box = driver.find_element_by_xpath("//form[input/@class='form-control ng-valid ng-valid-maxlength ng-not-empty ng-dirty ng-valid-parse ng-touched']")
#username_box = driver.find_element_by_class_name("hstack narrow-gap")
#username_box.send_keys("Sanjay")

#lastname_box=driver.find_element_by_id('lastname')
#lastname_box.send_keys("Nagaraj")

#email_box = driver.find_element_by_id('email')
#email_box.send_keys("s.nagaraj1628@gmail.com")

time.sleep(5)
#submit_button = driver.find_element_by_class_name('btn btn-lg btn-success ng-binding')
submit_button = driver.find_element_by_xpath("//button[contains(.,'Sign Up Now')]")
submit_button.click()

#username_box = driver.find_element_by_id("i0116")
#username_box.send_keys(usr)

#next_button = driver.find_element_by_id("idSIButton9")
#next_button.click()

#time.sleep(3)

#password_box = driver.find_element_by_id("i0118")
#password_box.send_keys(pwd)

#login_button = driver.find_element_by_id("idSIButton9")
#login_button.click()	

#url = "https://fortbendisd.schoology.com/course/2174800011/updates"
#response = requests.get(url)
#soup = BeautifulSoup(response.text, “html.parser”)


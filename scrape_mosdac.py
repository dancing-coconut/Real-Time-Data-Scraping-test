import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import numpy as np
import cv2

# while True: 
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.get('https://mosdac.gov.in/live/index_one.php?url_name=india')

time.sleep(5)

button = driver.find_element(By.XPATH, '//*[@id="bottom_menu_act_btn3"]')
button.click()

time.sleep(5)

dropdown_element = driver.find_element(By.XPATH, '//*[@id="canvas-layout"]/div[1]/div[2]/select')

select = Select(dropdown_element)
select.select_by_value("string:boxfill/nhc")

time.sleep(5)

full_screen = driver.find_element(By.XPATH, '//*[@id="map"]/div/div[2]/div[7]/button')
full_screen.click()

driver.save_screenshot('screenshot_ir.png')

full_screen = driver.find_element(By.XPATH, '//*[@id="map"]/div/div[2]/div[7]/button')
full_screen.click()

select.select_by_value("string:boxfill/greyscale")

time.sleep(5)

button = driver.find_element(By.XPATH, '//*[@id="bottom_menu_act_btn3"]')
button.click()

button = driver.find_element(By.XPATH, '//*[@id="bottom_menu_act_btn1"]')
button.click()

button = driver.find_element(By.XPATH, '//*[@id="bottom_menu_btn1"]/table/tbody/tr[1]/td[1]/button')
button.click()

time.sleep(5)

full_screen = driver.find_element(By.XPATH, '//*[@id="map"]/div/div[2]/div[7]/button')
full_screen.click()

time.sleep(5)

driver.save_screenshot('screenshot_wind.png')

driver.quit()
time.sleep(5)
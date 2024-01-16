import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import numpy as np
import cv2

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.get('https://mosdac.gov.in/live/index_one.php?url_name=india')

time.sleep(5)

button = driver.find_element(By.XPATH, '//*[@id="side_btn"]/table/tbody/tr/td[1]/button')
button.click()

input_element = driver.find_element(By.XPATH, '//md-checkbox[@aria-label="TIR1 Count"]//following-sibling::input')
input_element.send_keys(Keys.ARROW_RIGHT * 100)
button = driver.find_element(By.XPATH, '//*[@id="side_btn"]/table/tbody/tr/td[1]/button')
button.click()
full_screen = driver.find_element(By.XPATH, '//*[@id="map"]/div/div[2]/div[7]/button')
full_screen.click()

time.sleep(5)
driver.save_screenshot('screenshot.png')
driver.quit()

img = cv2.imread('screenshot.png')
lower_boundary = np.array([0, 100, 0]) 
upper_boundary = np.array([100, 255, 100]) 
mask = cv2.inRange(img, lower_boundary, upper_boundary)
new_color = np.array([255, 255, 255]) 
img[mask != 0] = new_color

height, width = img.shape[:2]
top = int(height / 3)
left = int(width * (7/28))
right = int(width - (width * (5/14)))
bottom = height

img_cropped = img[top:bottom, left:right]
cv2.imwrite('screenshot.png', img_cropped)



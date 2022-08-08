from re import A
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('http://www.pbclibrary.org/raton/mousercise.htm')
driver.maximize_window()

time.sleep(5)

levels=2
for i in range(1,levels):
  path = './/form[@action="m{}.htm"]'.format(str(i))
  element = driver.find_element(By.XPATH, path)
  element.click()
  time.sleep(4)

levels=16
for i in range(2,levels):
  path = './/a[@href="m{}.htm"]'.format(str(i))
  element = driver.find_element(By.XPATH, path)
  element.click()
  time.sleep(4)

levels=22
for i in range(17,levels):
  path = './/form[@action="m{}.htm"]'.format(str(i))
  element = driver.find_element(By.XPATH, path)
  element.click()
  time.sleep(4)


levels=23
for i in range(22,levels):
  path = './/a[@href="m{}.htm"]'.format(str(i))
  element = driver.find_element(By.XPATH, path)
  element.click()
  time.sleep(4)






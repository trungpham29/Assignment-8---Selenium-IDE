from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("C:\chromedriver/chromedriver.exe")
driver.get("http://automationpractice.com/index.php")

login1 = driver.find_element_by_xpath("/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a").click()
login2 = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button/span").click()
gmail = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div[2]/div[2]/form/div/div[1]/input")
gmail.send_keys("tp012341@gmail.com")
login3 = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button/span").click()



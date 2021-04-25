from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("C:\chromedriver/chromedriver.exe")
driver.get("http://www.practiceselenium.com/practice-form.html")

firstname = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[11]/div/form/fieldset/div[1]/p[2]/input")
firstname.send_keys("Huong")
lastname = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[11]/div/form/fieldset/div[1]/p[3]/input")
lastname.send_keys("Nguyen Thi")
sex = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[11]/div/form/fieldset/div[2]/p[2]/input[2]").is_selected()
sex = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[11]/div/form/fieldset/div[2]/p[2]/input[2]").click()
year = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[11]/div/form/fieldset/div[3]/p[2]/input[7]").is_selected()
year = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[11]/div/form/fieldset/div[3]/p[2]/input[7]").click()
favor = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[11]/div/form/fieldset/div[4]/p[2]/input[1]").click()
favor = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[11]/div/form/fieldset/div[4]/p[2]/input[2]").click()
chai = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[11]/div/form/fieldset/div[6]/p[2]/input").click()
chai = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[11]/div/form/fieldset/div[6]/p[3]/input").click()
area = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[11]/div/form/fieldset/div[7]/div/select")
area.send_keys("Asia")
final = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[11]/div/form/fieldset/div[8]/div/select/option[1]").click()
sub = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[11]/div/form/fieldset/div[9]/div/button").click()


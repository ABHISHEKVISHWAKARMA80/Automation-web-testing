from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:/Users/hp/Downloads/chromedriver.exe")
driver.maximize_window()
driver.get("http://172.27.16.216/filetracking/inward/")
driver.find_element_by_name("login").send_keys("2017016@iiitdmj.ac.in")
driver.find_element_by_id("id_password").send_keys(";=@?2Rh")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_element_by_xpath("//button[@class='ui primary button']").click()
driver.find_element_by_link_text("View").click()

driver.find_element_by_link_text("Attachments").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='header']").click()
time.sleep(2)
driver.find_element_by_link_text("Note Sheet").click()
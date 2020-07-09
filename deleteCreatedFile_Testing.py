from selenium import webdriver
from selenium.webdriver.support.select import Select
import  time

driver = webdriver.Chrome("C:/Users/hp/Downloads/chromedriver.exe")
driver.maximize_window()
driver.get("http://172.27.16.216/filetracking/drafts/")
driver.find_element_by_name("login").send_keys("2017016@iiitdmj.ac.in")
driver.find_element_by_id("id_password").send_keys(";=@?2Rh")
driver.find_element_by_xpath("//button[@type='submit']").click()

#time.sleep(2)

driver.find_element_by_xpath("//button[@class='ui primary button']").click()
driver.find_element_by_link_text("Delete").click()
driver.find_element_by_link_text("Delete").click()

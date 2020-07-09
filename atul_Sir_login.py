from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:/Users/hp/Downloads/chromedriver.exe")
driver.maximize_window()
driver.get("http://172.27.16.216/filetracking/inward/")
driver.find_element_by_name("login").send_keys("atul")
driver.find_element_by_id("id_password").send_keys("hello123")
driver.find_element_by_xpath("//button[@type='submit']").click()
#driver.find_element_by_link_text("shivdayal - hall4caretaker").click()
driver.find_element_by_xpath("//button[@class='ui primary button']").click()
driver.find_element_by_link_text("View").click()

driver.find_element_by_xpath("//textarea[@name='remarks']").send_keys("for MCM scholarship")
driver.find_element_by_xpath("//input[@name='receiver']").send_keys("2017054")
driver.find_element_by_id("input_search1").send_keys("student")
driver.find_element_by_id("file").send_keys("C:/SEMESTER/SEMESTER 6/MACHINE LEARNING/Project/my notes for presentation/image.jpg")
time.sleep(3)
driver.find_element_by_xpath("//button[@name='send']").click()
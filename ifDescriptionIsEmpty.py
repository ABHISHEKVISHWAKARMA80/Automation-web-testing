from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/hp/Downloads/chromedriver.exe")
driver.maximize_window()
driver.get("http://172.27.16.216/filetracking/")
driver.find_element_by_name("login").send_keys("2017016@iiitdmj.ac.in")
driver.find_element_by_id("id_password").send_keys(";=@?2Rh")
driver.find_element_by_xpath("//button[@type='submit']").click()

driver.find_element_by_name("title").send_keys("Bonafide Certificate")
driver.implicitly_wait(5)

driver.implicitly_wait(1000)
#"2017016 - student"

driver.find_element_by_id("file").send_keys("C:/SEMESTER/SEMESTER 6/MACHINE LEARNING/Project/my notes for presentation/image.jpg")

driver.find_element_by_xpath("//textarea[@name='remarks']").send_keys("for MCM scholarship")
driver.find_element_by_xpath("//input[@name='receiver']").send_keys("2017040")
driver.find_element_by_id("input_search1").send_keys("student")
driver.find_element_by_xpath("//button[@name='send']").click()
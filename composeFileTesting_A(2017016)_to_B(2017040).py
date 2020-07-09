from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:/Users/hp/Downloads/chromedriver.exe")
driver.maximize_window()
driver.get("http://172.27.16.216/")
driver.find_element_by_xpath("//a[@class='ui primary large button']").click()
driver.find_element_by_name("login").send_keys("2017016@iiitdmj.ac.in")
driver.find_element_by_id("id_password").send_keys(";=@?2Rh")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.implicitly_wait(10)

driver.find_element_by_xpath("//i[@class='sidebar icon']").click()
time.sleep(2)
driver.find_elements_by_partial_link_text('File Tracking')[0].click()
driver.implicitly_wait(1000)

#driver.find_elements_by_partial_link_text('Compose File')[0].click()
driver.find_element_by_name("title").send_keys("Bonafide Certificate")
driver.find_element_by_name("desc").send_keys("A bonafide certificate is a certificate issued by the School/ college to prove that the student has studied in a particular school/ college during the period so and so to prove that the student continued studies and resided in a particular location.")
driver.implicitly_wait(5)

#driver.find_element_by_class_name("text").click()
obj = Select(driver.find_element_by_name("design"))
obj.select_by_value("1406")

driver.implicitly_wait(1000)
#"2017016 - student"

driver.find_element_by_id("file").send_keys("C:/SEMESTER/SEMESTER 6/MACHINE LEARNING/Project/my notes for presentation/image.jpg")

driver.find_element_by_xpath("//textarea[@name='remarks']").send_keys("for MCM scholarship")
driver.find_element_by_xpath("//input[@name='receiver']").send_keys("2017040")
driver.find_element_by_id("input_search1").send_keys("student")
time.sleep(3)
driver.find_element_by_xpath("//button[@name='send']").click()
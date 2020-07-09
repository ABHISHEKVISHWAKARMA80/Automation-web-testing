from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:/Users/hp/Downloads/chromedriver.exe")
driver.maximize_window()
driver.get("http://172.27.16.216/filetracking/")
driver.find_element_by_name("login").send_keys("kusum@iiitdmj.ac.in")
driver.find_element_by_id("id_password").send_keys("_rX'~cs")
driver.find_element_by_xpath("//button[@type='submit']").click()
#driver.find_element_by_xpath("//button[@class='ui primary button']").click()
#driver.find_element_by_link_text("shivdayal - hall4caretaker").click()
#driver.find_element_by_link_text("View").click()

driver.find_element_by_name("title").send_keys("Regarding Entry and exit time of girls in HALL-4")
driver.find_element_by_name("desc").send_keys("Even now though there’s a one-hour gap between timings, with girls expected to report back to their hostels at 11pm instead of 10pm earlier.")
driver.find_element_by_xpath("//textarea[@name='remarks']").send_keys("for official permission")
driver.find_element_by_xpath("//input[@name='receiver']").send_keys("shivdayal")
driver.find_element_by_id("input_search1").send_keys("hall4caretaker")
driver.find_element_by_id("file").send_keys("C:/SEMESTER/SEMESTER 6/MACHINE LEARNING/Project/my notes for presentation/image.jpg")
time.sleep(2)
driver.find_element_by_xpath("//button[@name='send']").click()

###################################################################################################################################

driver.find_element_by_link_text("Logout").click()
driver.find_element_by_xpath("//button[@class='ui right floated positive button']").click()
driver.find_element_by_name("login").send_keys("shivdayal@iiitdmj.ac.in")
driver.find_element_by_id("id_password").send_keys("SWVBPK5")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//i[@class='sidebar icon']").click()

time.sleep(2)
driver.find_elements_by_partial_link_text('File Tracking')[0].click()
driver.find_element_by_link_text("Inbox").click()
#driver.find_element_by_xpath("//button[@class='ui primary button']").click()
driver.find_element_by_link_text("shivdayal - hall4caretaker").click()
driver.find_element_by_link_text("View").click()

driver.find_element_by_xpath("//textarea[@name='remarks']").send_keys("Ok, I have changed the timing and official permission is attached")
driver.find_element_by_xpath("//input[@name='receiver']").send_keys("kusum")
driver.find_element_by_id("input_search1").send_keys("hall1caretaker")
driver.find_element_by_id("file").send_keys("C:/SEMESTER/SEMESTER 6/MACHINE LEARNING/Project/my notes for presentation/image.jpg")
time.sleep(2)
driver.find_element_by_xpath("//button[@name='send']").click()

######################################################################################################################################
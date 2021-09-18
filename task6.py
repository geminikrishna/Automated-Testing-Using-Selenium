
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("http://www.thesparksfoundation.sg")
time.sleep(5)
print("Test 1 Logo Check")
try:
    driver.find_element_by_css_selector("img[src='/images/logo_small.png']")
    print("Test 1 Pass : Logo is present\n")
except NoSuchElementException:
    print("Test 1 Fail : Logo is not present\n")
time.sleep(5)

print("Test 2 Title Match Check")
if(driver.title=="The Sparks Foundation | Home"):
    print("Test 2 Pass : Title is Matched\n")
else:
    print("Test 2 Fail : Title is Not Matched\n")
time.sleep(5)

print("Test 3 About Us Page Check")
try:
    driver.find_element_by_link_text("About Us").click()
    driver.find_element_by_link_text("Executive Team").click()
    print("Test 3 Pass : About Us/Executive Team Page Exists\n")
except NoSuchElementException:
    print("Test 3 Fail : About Us/Executive Team Page Does Not exist\n")
time.sleep(5)

print("Test 4 Policies Page Check")
try:
    driver.find_element_by_link_text("Policies and Code").click()
    driver.find_element_by_link_text("Policies").click()
    print("Test 4 Pass : Policies Page Exists\n")
except NoSuchElementException:
    print("Test 4 Fail : Policies Page Does Not exist\n")
time.sleep(5)

print("Test 5 Links Page Check")
try:
    driver.find_element_by_link_text("LINKS").click()
    driver.find_element_by_link_text("Salient Features").click()
    print("Test 5 Pass : LINKS/Salient Features Page Exists\n")
except NoSuchElementException:
    print("Test 5 Fail : LINKS/Salient Features Page Does Not exist\n")
time.sleep(5)

print("Test 6 Join Us Page Check")
try:
    driver.find_element_by_link_text("Join Us").click()
    driver.find_element_by_link_text("Internship Positions").click()
    print("Test 6 Pass : Join Us/Internship Positions Page Exists\n")
except NoSuchElementException:
    print("Test 6 Fail : Join Us/Internship Positions Page Does Not exist\n")
time.sleep(5)

print("Test 7 Contact Us Page Check")
try:
    driver.find_element_by_link_text("Contact Us").click()

    print("Test 7 Pass : Contact Us Page Exists\n")
except NoSuchElementException:
    print("Test 7 Fail : Contact Us Page Does Not exist\n")
time.sleep(5)

print("Test 8 Programs Page Check")
try:
    driver.find_element_by_link_text("Programs").click()
    driver.find_element_by_link_text("Student Scholarship Program").click()
    print("Test 8 Pass : Programs/Student Scholarship Program Page Exists\n")
except NoSuchElementException:
    print("Test 8 Fail : Programs/Student Scholarship Program Page Does Not exist\n")
time.sleep(5)

print("Test 9 Facebook Page Link Check")
try:
    driver.find_element_by_css_selector("a[href='https://www.facebook.com/thesparksfoundation.info']")
    print("Test 9 Pass : Facebook Page Link Exists\n")
except NoSuchElementException:
    print("Test 9 Fail : Facebook Page Link Does Not exist\n")
time.sleep(5)

print("Test 10 Instagram Page Link Check and open if it exists")
try:
    driver.find_element_by_css_selector("a[href='https://instagram.com/thesparksfoundation.info'").click()
    print("Test 10 Pass : Instagram Page Link Exists\n")
except NoSuchElementException:
    print("Test 10 Fail : Instagram Page Link Does Not exist\n")


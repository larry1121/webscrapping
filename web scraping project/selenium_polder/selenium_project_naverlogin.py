from selenium import webdriver
import time
browser = webdriver.Chrome(r"C:\Users\user\OneDrive\바탕 화면\python\web scraping project\selenium_polder\chromedriver.exe")
browser.get("http://naver.com")

elem=browser.find_element_by_class_name("link_login")

elem.click()

browser.find_element_by_id("id").send_keys("larry1121")
browser.find_element_by_id("pw").send_keys("psword")

browser.find_element_by_id("log.login").click()

time.sleep(3)

browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("아 안되네")

print(browser.page_source)

browser.quit()



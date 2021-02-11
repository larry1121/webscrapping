from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#드루감
browser = webdriver.Chrome(r"C:\Users\user\OneDrive\바탕 화면\python\web scraping project\selenium_polder\chromedriver.exe")
browser.get("https://flight.naver.com/flights/")

#
browser.find_element_by_link_text("가는날 선택").click()

browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("5")[1].click()

browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

browser.find_element_by_link_text("항공권 검색").click()


try:
  elem=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))  
  print(elem.text)
  #10초간 기다림.이 엘리멘트가 존재할때 까지만
except:
    browser.quit()
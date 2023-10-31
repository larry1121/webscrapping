import requests
from bs4 import BeautifulSoup#데이터탐색
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import urllib.request

from collections import Counter
from config import WEBDRIVER_PATH,USER_ID,PASSWORD

def login():

  URL="https://everytime.kr/login"

  browser = webdriver.Chrome(WEBDRIVER_PATH)
  browser.get(URL)

  elem_id=browser.find_element_by_name("userid")
  elem_id.click()
  elem_id.send_keys(USER_ID)
  elem_pw=browser.find_element_by_name("password")
  elem_pw.click()
  elem_pw.send_keys(PASSWORD)

  browser.find_element_by_class_name("submit").click()
  time.sleep(3)
  #login
  
  searchWindow=browser.find_element_by_xpath("//*[@id=\"container\"]/div[3]/form/input") 
  print("a")
  searchWindow.click()
  print("b")
  searchWindow.send_keys("만한곳")
  print("c")
  searchWindow.send_keys(Keys.RETURN)
  print("d")
  time.sleep(3)
  #검색어 입력

  
  

  count=1
  words=""
  while count<100:

    if(count==1):

      soup=BeautifulSoup(browser.page_source,"html.parser")

      articles=soup.find_all("a",{"class":["article"]})
      
      for article in articles:
          try:

            title=article.find("h2").text
            words= title + words
          except:
            pass

      time.sleep(1)
      browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

      try:
        banner_button=browser.find_element_by_xpath("//*[@id=\"sheet\"]/ul/li[3]/a") 
        time.sleep(5)
        banner_button.click()
      except:
        print("배너없음")


      next_page_button=browser.find_element_by_xpath("//*[@id=\"container\"]/div[2]/div[2]/a")
      count=count+1 
      
      
      
      next_page_button.click()
      time.sleep(1)

    elif(count >= 2):
      soup=BeautifulSoup(browser.page_source,"html.parser")

      articles=soup.find_all("a",{"class":["article"]})
      browser.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
      try:

        for article in articles:
          title=article.find("h2").get_text()
          words = words + title
      except:
          pass
      time.sleep(3)
      if (count >=4):
          next_page_button=browser.find_element_by_xpath("//*[@id=\"container\"]/div[2]/div[2]/a[3]")
      else:
          next_page_button=browser.find_element_by_xpath(f"//*[@id=\"container\"]/div[2]/div[2]/a[{count}]")
      count=count+1
     
      
      
      next_page_button.click()
      time.sleep(1)
    else:
        print("알 수없는 오류")

    
    

login()

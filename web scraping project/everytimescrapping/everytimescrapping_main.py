import requests
from bs4 import BeautifulSoup#데이터탐색
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import urllib.request
from konlpy.tag import Kkma
from konlpy.utils import pprint
from collections import Counter
from konlpy.tag import Kkma
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
  free_board=browser.find_element_by_xpath("//*[@id=\"container\"]/div[4]/div[1]/div/h3/a")
  free_board.click()
  time.sleep(2)
  count=1
  words=""
  while count<10:

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
      
      time.sleep(5)
      # try:
      #   banner_button=browser.find_element_by_xpath("//*[@id=\"sheet\"]/ul/li[3]/a") 

      #   banner_button.click()
      # except:
      #   print("no banner")
      #   continue
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

  # print(words)
  
  kkma = Kkma()
  Nouns=kkma.nouns(words)



  count = Counter(Nouns) 
  tag_count = []

  tags = []



  for n, c in count.most_common(100):

	  dics = {'tag': n, 'count': c}

	  if len(dics['tag']) >= 2 and len(tags) <= 49:

	      tag_count.append(dics)

	      tags.append(dics['tag'])

	

  for tag in tag_count:


      print(" {:<14}".format(tag['tag']), end='\t')

      print("{}".format(tag['count']))






  print("명사 총  {}개".format(len(tags)))

  b={}
  for a in tag_count:


    b[a["tag"]]=a["count"]
        
    
  return b
  
  time.sleep(99)
#click사이에 딜레이 넣으니까 오류해결


login()
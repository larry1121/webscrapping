import requests
from bs4 import BeautifulSoup#데이터탐색
LIMIT=50
URL=f"https://kr.indeed.com/jobs?q=python&l=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&radius=100&limit={LIMIT}"

def get_last_page():
    resul=requests.get(URL)

    soup=BeautifulSoup(resul.text,"html.parser")

    pagination=soup.find("ul",{"class":"pagination-list"})
    print(type(pagination))

    links=pagination.find_all('a')#anchor 웹페이지간 연결

    spans=[]

    for link in links[:-1]:
        spans.append(int(link.find("span").string)) #span을찾고 그안의 스트링 가져오기
    max_page=spans[-1]
    return max_page 

def extract_jobs(last_page):
    
    jobs=[]
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result=requests.get(f"{URL}&start={page*LIMIT}")
        soup=BeautifulSoup(result.text,"html.parser")
        results=soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
        for result in results:
            job=extract_job(result)
            jobs.append(job)
            
            
    return jobs
    

def extract_job(html):
    title=html.find("h2", {"class":"title"}).find('a')["title"]
    company=html.find("span",{"class":"company"})
    company_anchor=company.find("a")
    if company_anchor is not None:
        company=str(company_anchor.string)
    else:
        company=str(company.string)
        company=company.strip()
    location=html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
    job_id=html["data-jk"]
    return {"title":title,"company":company,"location":location,"link":f"https://kr.indeed.com/viewjob?jk={job_id}"}


def Get_jobs():
    last_page=get_last_page()
    jobs=extract_jobs(last_page)
    return jobs



    # for n in range(max_page):
    #     print(f"start{n*50}")
    


# 1) request.get으로 indeed 사이트를 가져옴.
# 2) BeautifulSoup으로 indeed_result.text의 html 정보를 가져옴.
# 3) pagination이라는 변수를 설정해, Indeed_soup에서 pagination이라는 이름을 가진 div를 가져옴.
# 4) pages라는 변수를 설정해, pagination 속에 있는 a를 찾아 리스트로 만듬 (find_all)
# 5) spans=[]라는 빈 리스트를 설정한 후, for loop를 이용하여 4)의 pages안에서 span을 찾아 spans라는 리스트에 담아줌.
# 6) spans 리스트에서 마지막번째 item를 제외해줌. (spans[:-1])
# - anchor 안에 하나의 span 만 있고, 그 안에 하나의 string만 있기 때문에,
# 바로 anchor에 string method을 적용해도 작동한다.
# - str을 int로 변환하기 위해, for 문에서 links[:-1]을 먼저 해줘서 마지막 item을 제외시킨 뒤, int함수를 걸어준다.
# - 최대 페이지를 변수화해준다
# - 각 페이지마다 계속해서 request하는 법을 알아야 함 (다음 영상)

# 1. 모든 a 태그 검색
# soup.find_all("a")
# soup("a")

# 2. string 이 있는 title 태그 모두 검색
# soup.title.find_all(string=True)
# soup.title(string=True)

# 3. a 태그를 두개만 가져옴
# soup.find_all("a", limit=2)

# 4. string 검색
# soup.find_all(string="Elsie") # string 이 Elsie 인 것 찾기
# soup.find_all(string=["Tillie", "Elsie", "Lacie"]) # or 검색
# soup.find_all(string=re.compile("Dormouse")) # 정규식 이용

# 5. p 태그와 속성 값이 title 이 있는거
# soup.find_all("p", "title")
# 예)

# 6. a태그와 b태그 찾기
# soup.find_all(["a", "b"])

# 7. 속성 값 가져오기
# soup.p['class']
# soup.p['id']

# 8. string을 다른 string으로 교체
# tag.string.replace_with("새로운 값")

# 9. 보기 좋게 출력
# soup.b.prettify()

# 10. 간단한 검색
# soup.body.b # body 태그 아래의 첫번째 b 태그
# soup.a # 첫번째 a 태그

# 11. 속성 값 모두 출력
# tag.attrs

# 12. class 는 파이썬에서 예약어이므로 class_ 로 쓴다.
# soup.find_all("a", class_="sister")

# 13. find
# find()
# find_next()
# find_all()

# 14. find 할 때 확인
# if soup.find("div", title=True) is not None:
# i = soup.find("div", title=True)

# 15. data-로 시작하는 속성 find
# soup.find("div", attrs={"data-value": True})

# 16. 태그명 얻기
# soup.find("div").name

# 17. 속성 얻기
# soup.find("div")['class'] # 만약 속성 값이 없다면 에러
# soup.find("div").get('class') # 속성 값이 없다면 None 반환

# 18. 속성이 있는지 확인
# tag.has_attr('class')
# tag.has_attr('id')
# 있으면 True, 없으면 False

# 19. 태그 삭제
# a_tag.img.unwrap()

# 20. 태그 추가
# soup.p.string.wrap(soup.new_tag("b"))
# soup.p.wrap(soup.new_tag("div"




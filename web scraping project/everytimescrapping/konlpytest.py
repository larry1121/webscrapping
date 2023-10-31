from konlpy.tag import Kkma
from konlpy.utils import pprint
from collections import Counter
from wordcloud import WordCloud
# from crawling import load_counts_file, crawl_word_counts

def konlpy_test():


    kkma = Kkma()



    f = open(r"web scraping project/everytimescrapping/Blog.txt", mode= 'r', encoding = "utf-8")

    lines = f.read()
    Nouns=kkma.nouns(lines)



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



    # tags = tag_counting(file = "blog.txt")

    #print(tags)

    f.close()
    # print(tag_count)
    b={}
    for a in tag_count:
        b[a["tag"]]=a["count"]
        
    print(b)
    return b
konlpy_test()
# https://github.com/konlpy/konlpy/issues/349 이슈보고 두 줄 주석처리하고 해결
#문자열앞에 r붙여주면 탈출문자로 오인되는 문제 해결 ㄱㄴ
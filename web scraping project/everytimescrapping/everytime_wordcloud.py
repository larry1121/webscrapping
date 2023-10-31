from wordcloud import WordCloud
from everytimescrapping_main import login
word_counts=login()
print("scrapping finish")
wc = WordCloud(font_path=r'C:\Users\user\OneDrive\바탕 화면\python\web scraping project\everytimescrapping\NanumGothic.ttf',background_color='white',width=800,height=800)
wc_img = wc.generate_from_frequencies(word_counts)
wc_img.to_file('everytime_wordcloud.jpg')
print('finish')


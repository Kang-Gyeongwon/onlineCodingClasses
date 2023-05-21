import requests
from bs4 import BeautifulSoup

URL = "https://movie.daum.net/ranking/reservation"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# 특정 제목 가져오기
title = soup.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child(6) > div > div.thumb_cont > strong > a')
print(title.text)       # 태그 안에 텍스트를 보여줌
print(title['href'])    # 태그 안에 속성의 값을 보여줌

# 제목만 추출해오기
lis = soup.select('#mainContent > div > div.box_ranking > ol > li')

for li in lis:
    title = li.select_one('.link_txt')
    print(title.text)
    # 아래와 같은 코드
    # title = li.select_one('.link_txt').text
    # print(title)

# 순위, 평점 가져오기
lis = soup.select('#mainContent > div > div.box_ranking > ol > li')

# print(lis)

for li in lis:
    rank = li.select_one('.rank_num').text
    title = li.select_one('.link_txt').text
    rate = li.select_one('.txt_grade').text
    print(rank, title, rate)
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

#=================


# 여기부터 숙제

# select를 이용해서, tr들을 불러오기
songs = soup.select('#body-content > div.newest-list > div.music-list-wrap > table.list-wrap > tbody > tr')

# songs(tr들) 의 반복문을 돌리기
for song in songs:

    origin_number_1 = song.select_one('td.number').text
    origin_number_2 = origin_number_1.split( )
    number = origin_number_2[0]
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    singer = song.select_one('td.info > a.artist.ellipsis').text
    
    print(number,title,singer)      
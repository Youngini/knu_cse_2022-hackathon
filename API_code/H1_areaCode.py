import requests
from bs4 import BeautifulSoup
import pandas as pd
import xml.etree.ElementTree as ET

# URL = 'http://apis.data.go.kr/B551011/KorWithService/areaCode?serviceKey=gZjpfTAl8ER3T1iBD80scD9b%2FOJyXAGkYsuD%2BAcLVziyqpxC5OTUZAjUws3IMQiXk%2FSFdlrpy%2FzBCZ9S5Q51Gg%3D%3D&MobileOS=ETC&MobileApp=AppTest'
# 대구 코드 4임
URL = 'http://apis.data.go.kr/B551011/KorWithService/areaCode?serviceKey=gZjpfTAl8ER3T1iBD80scD9b%2FOJyXAGkYsuD%2BAcLVziyqpxC5OTUZAjUws3IMQiXk%2FSFdlrpy%2FzBCZ9S5Q51Gg%3D%3D&MobileOS=ETC&MobileApp=AppTest&areaCode=4'
rq = requests.get(URL)
soup = rq.text

data = BeautifulSoup(soup,'xml')
rows = data.find_all('item')

row = []

for x in rows:
    a = (x.find('rnum'))
    b = (x.find('code'))
    c = (x.find('name'))
    row.append([a.get_text(),b.get_text(),c.get_text()])

df = pd.DataFrame(row,columns=['rnum','code','name'])
print(row)
print(df)
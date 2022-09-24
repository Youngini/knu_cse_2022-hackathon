import requests
from bs4 import BeautifulSoup
import pandas as pd
import xml.etree.ElementTree as ET

URL = 'http://apis.data.go.kr/B551011/KorWithService/areaBasedList?serviceKey=gZjpfTAl8ER3T1iBD80scD9b%2FOJyXAGkYsuD%2BAcLVziyqpxC5OTUZAjUws3IMQiXk%2FSFdlrpy%2FzBCZ9S5Q51Gg%3D%3D&MobileOS=ETC&MobileApp=AppTest&areaCode=4'
rq = requests.get(URL)
soup = rq.text
data = BeautifulSoup(soup,'xml')
rows = data.find_all('item')

row = []

for x in rows:
    a = (x.find('addr1'))
    b = (x.find('addr2'))
    c = (x.find('areacode'))
    d = (x.find('booktour'))
    e = (x.find('cat1'))
    f = (x.find('cat2'))
    g = (x.find('cat3'))
    h = (x.find('contentid'))
    i = (x.find('contenttypeid'))
    j = (x.find('createdtime'))
    k = (x.find('firstimage'))
    l = (x.find('firstimage2'))
    m = (x.find('mapx'))
    n = (x.find('mapy'))
    o = (x.find('mlevel'))
    p = (x.find('modifiedtime'))
    q = (x.find('readcount'))
    r = (x.find('sigungucode'))
    s = (x.find('tel'))
    t = (x.find('title'))
    u = (x.find('zipcode'))
    row.append([a.get_text(),b.get_text(),c.get_text(),d.get_text(),e.get_text(),f.get_text(),g.get_text(),h.get_text(),i.get_text(),j.get_text(),k.get_text(),l.get_text(),m.get_text(),n.get_text(),o.get_text(),p.get_text(),q.get_text(),r.get_text(),s.get_text(),t.get_text(),u.get_text()])

df = pd.DataFrame(row,columns=['addr1','addr2','areacode','booktour','cat1','cat2','cat3','contentid','contenttypeid','createdtime','firstimage','firstimage2','mapx','mapy','mlevel','modifiedtime','readcount','sigungucode','tel','title','zipcode'])
print(df)
df.to_excel(excel_writer='areaBasedList.xlsx')
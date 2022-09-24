from asyncio import set_child_watcher
import requests
from bs4 import BeautifulSoup
import pandas as pd

set = ['addr1','addr2','areacode','booktour','cat1','cat2','cat3','contentid','contenttypeid','createdtime','firstimage','firstimage2','mapx','mapy','mlevel','modifiedtime','readcount','sigungucode','tel','title','zipcode','showflag']

URL = 'http://apis.data.go.kr/B551011/KorWithService/areaBasedSyncList?serviceKey=gZjpfTAl8ER3T1iBD80scD9b%2FOJyXAGkYsuD%2BAcLVziyqpxC5OTUZAjUws3IMQiXk%2FSFdlrpy%2FzBCZ9S5Q51Gg%3D%3D&MobileOS=ETC&MobileApp=AppTest&areaCode=4'
rq = requests.get(URL)
soup = rq.text
data = BeautifulSoup(soup,'xml')
rows = data.find_all('item')
row=[]
for x in rows:
    arr = []
    tem = []
    for y in set:
        arr.append(x.find(y))
    
    for z in arr:
        if(z!=None):
            tem.append(z.get_text())
        else:
            tem.append(' ')

    row.append(tem)

df = pd.DataFrame(row,columns = set)
print(df)
df.to_excel(excel_writer='areaBasedSyncList.xlsx')

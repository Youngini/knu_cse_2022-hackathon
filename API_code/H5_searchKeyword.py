import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'http://apis.data.go.kr/B551011/KorWithService/searchKeyword?serviceKey=gZjpfTAl8ER3T1iBD80scD9b%2FOJyXAGkYsuD%2BAcLVziyqpxC5OTUZAjUws3IMQiXk%2FSFdlrpy%2FzBCZ9S5Q51Gg%3D%3D&MobileOS=ETC&MobileApp=AppTest&keyword=대구'
rq = requests.get(URL)
soup = rq.text
data = BeautifulSoup(soup,'xml')
rows = data.find_all('item')
set = ['addr1','addr2','areacode','booktour','cat1','cat2','cat3','contentid','contenttypeid','createdtime','firstimage','firstimage2','mapx','mapy','mlevel','modifiedtime','readcount','sigungucode','tel','title']
row = []

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
print(row)
df = pd.DataFrame(row,columns = set)
print(df)
df.to_excel(excel_writer='searchKeyword.xlsx')
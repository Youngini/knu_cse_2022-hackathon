from asyncio import set_child_watcher
import requests
from bs4 import BeautifulSoup
import pandas as pd

set = ['contentid','originimgurl','imgname','smallimageurl','serialnum']
contentid_excel = pd.read_excel('detailIntro.xlsx',usecols=[1])

contentid = contentid_excel.values.tolist()

URL = 'http://apis.data.go.kr/B551011/KorWithService/detailImage?serviceKey=gZjpfTAl8ER3T1iBD80scD9b%2FOJyXAGkYsuD%2BAcLVziyqpxC5OTUZAjUws3IMQiXk%2FSFdlrpy%2FzBCZ9S5Q51Gg%3D%3D&MobileOS=ETC&MobileApp=AppTest'
row = []
for x in range(len(contentid)):
    contents = '&contentId='+str(*contentid[x])
    rq = requests.get(URL,contents)
    soup = rq.text
    data = BeautifulSoup(soup,'xml')
    rows = data.find_all('item')
    if(rows == []):
        continue
    else:
        for i in rows:
            # 값 저장 시작
            arr = []
            tem = []
            for y in set:
                arr.append(i.find(y))
            
            for z in arr:
                if(z!=None):
                    tem.append(z.get_text())
                else:
                    tem.append(' ')

            row.append(tem)

df = pd.DataFrame(row,columns = set)
print(df)
df.to_excel(excel_writer='detailImage.xlsx')

    

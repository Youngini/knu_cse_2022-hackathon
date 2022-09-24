from asyncio import set_child_watcher
import requests
from bs4 import BeautifulSoup
import pandas as pd

set = ['contentid','contenttypeid','account','chkbabycarriage','chkcreditcard','chkpet','expagerange','expguide','heritage1','heritage2','heritage3','infocenter','opendate','parking','restdate','useseason','usetime']
local_contentid_excel = pd.read_excel('locationBasedList.xlsx',usecols=[8])
local_contenttypeid_excel= pd.read_excel('locationBasedList.xlsx',usecols=[9])

local_contentid = local_contentid_excel.values.tolist()
local_contenttypeid = local_contenttypeid_excel.values.tolist()

URL = 'http://apis.data.go.kr/B551011/KorWithService/detailIntro?serviceKey=gZjpfTAl8ER3T1iBD80scD9b%2FOJyXAGkYsuD%2BAcLVziyqpxC5OTUZAjUws3IMQiXk%2FSFdlrpy%2FzBCZ9S5Q51Gg%3D%3D&MobileOS=ETC&MobileApp=AppTest' 
row = []
for x in range(len(local_contentid)):
    # 엑셀에서 추출한 데이터 사용
    contents = '&contentId='+str(*local_contentid[x])+'&contentTypeId='+str(*local_contenttypeid[x])
    rq = requests.get(URL,contents)
    soup = rq.text
    data = BeautifulSoup(soup,'xml')
    rows = data.find('item')
    # 값 저장 시작
    arr = []
    tem = []
    for y in set:
        arr.append(rows.find(y))
    
    for z in arr:
        if(z!=None):
            tem.append(z.get_text())
        else:
            tem.append(' ')

    row.append(tem)

# 두번째 데이터
search_contentid_excel = pd.read_excel('searchKeyword.xlsx',usecols=[8])
search_contenttypeid_excel= pd.read_excel('searchKeyword.xlsx',usecols=[9])

search_contentid = search_contentid_excel.values.tolist()
search_contenttypeid = search_contenttypeid_excel.values.tolist()

for x in range(len(search_contentid)):
    # 엑셀에서 추출한 데이터 사용
    contents = '&contentId='+str(*search_contentid[x])+'&contentTypeId='+str(*search_contenttypeid[x])
    rq = requests.get(URL,contents)
    soup = rq.text
    data = BeautifulSoup(soup,'xml')
    rows = data.find('item')
    # 값 저장 시작
    arr = []
    tem = []
    for y in set:
        arr.append(rows.find(y))
    
    for z in arr:
        if(z!=None):
            tem.append(z.get_text())
        else:
            tem.append(' ')

    row.append(tem)

df = pd.DataFrame(row,columns = set)
print(df)
df.to_excel(excel_writer='detailIntro.xlsx')



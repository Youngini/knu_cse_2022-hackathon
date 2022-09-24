import pandas as pd
# 엑셀에서 카테고리 데이터 가져오기
filename = 'open_api.xlsx'
category_excel = pd.read_excel(filename,sheet_name='H2_categoryCode',names = ['Category'],usecols=[3])
category = category_excel.values.tolist()

for i in range(len(category)):
    a = str(*category[i])

# 엑셀에서 카테고리에 맞는 장소 가져오기
place_excel = pd.read_excel(filename,sheet_name='H3_areaBasedList',usecols=[1])
place_cate_excel = pd.read_excel(filename,sheet_name='H3_areaBasedList',usecols=[6])
location_excel = pd.read_excel(filename,sheet_name='H3_areaBasedList',usecols=[2])
place = place_excel.values.tolist()
place_cate = place_cate_excel.values.tolist()
location = location_excel.values.tolist()

for i in range(len(place)):
    a = str(*place[i])
    b = str(*place_cate[i])
    c = str(*location[i])

    if(b == 'A01'):
        k = '자연'
    elif(b == 'A02'):
        k = '인문(문화/예술/역사)'        
    elif( b== 'A03'):
        k = '레포츠'
    elif(b == 'A04'):
        k = '쇼핑'
    elif(b == 'A05'):
        k = '음식'
    elif(b == 'B02'):
        k = '숙박'
    else:
        k = '추천코스'


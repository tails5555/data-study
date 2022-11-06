# 데이터 참조 : http://data.seoul.go.kr/dataList/OA-12252/S/1/datasetView.do

# 각 지하철 역별 승하차 인원 총계 취합 (Row : 지하철역, Col : 년월 )

import pandas as pd

df = pd.read_csv("./서울시 지하철 호선별 역별 시간대별 승하차 인원 정보.csv", encoding='cp949')

df_pivot = df.copy()

df_pivot['총 승차인원'] = 0

df_pivot['총 하차인원'] = 0

for index in list(df_pivot):
    if index.endswith('승차인원'):
        df_pivot['총 승차인원'] += df_pivot[index]
    if index.endswith('하차인원'):
        df_pivot['총 하차인원'] += df_pivot[index]

# 피벗 테이블 생성 - 승차 / 하차 이렇게 나뉠 것이다.
df_pivot = df_pivot.pivot_table(
    values = ['총 승차인원', '총 하차인원'],
    index = '지하철역',
    columns = '사용월',
    aggfunc = 'sum'
)

df_pivot.to_excel('output.xlsx', sheet_name='승하차_취합')

print(df_pivot)

# 유의 사항 : 결측값이 나올 수도 있다. 사유는 아래와 같다.
# - 일부 지하철 역에 대해 개통이 이뤄지지 않았을 경우 (ex. 신림선 - 서울지방병무청역은 2022년 5월 이후 개통되어 이전 데이터는 NaN 이 나옴.)
# - 일부 지하철 역에 대해 측정이 이뤄지지 않았을 경우
# - 인구 측정 중 천재지변으로 인한 작업 중단이 발생한 경우 등
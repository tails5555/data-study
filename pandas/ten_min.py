import numpy as np

import pandas as pd

# 숫자형 데이터의 기본 타입은 Double 형으로 생각하면 된다.
s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)

# 날짜형 데이터는 YYYYMMDD 이런 식으로 받는가보다.
dates = pd.date_range("20221101", periods=7)

print(dates)

# 위에서 만든 날짜 데이터들을 통해 랜덤 숫자로 DataFrame 형을 취합시킬 수 있다.
# 위에 만들어졌던 데이터 타입들은 Series 형.
# randn 은 랜덤 숫자 (아무 실수 값, Row 개수 * Col 개수 이렇게 정의 시켜줘야 한다.)
df = pd.DataFrame(np.random.randn(7, 6), index=dates, columns=list("ABCDEF"))

print(df)

# DataFrame 은 아래와 같이 초기화 시켜 생성할 수 있다. 단, 각 요소에 들어가는 값들은 열 별로 데이터 타입이 달라질 수도 있다.
df2 = pd.DataFrame(
    {
        "A": 1.0, # 실수 값 (연속값)
        "B": pd.Timestamp("20221101"), # 날짜 값 (시계열 값)
        "C": pd.Series(15, index=list(range(4)), dtype="float32"), # 실수 값 (연속값)
        "D": np.array([4] * 4, dtype="int32"), # 정수 값 (연속 값)
        "E": pd.Categorical(["Chun", "Jat", "Cap", "Baaaaap"]), # 범주 값
        "F": "mTE", # 객체 값 주입 (연속값, 범주값 두 가지를 넣는 것을 권장하나 보다.)
    }
)

print(df2)

# DataFrame 타입은 아래와 같이 추론할 수 있다.
print(df2.dtypes)

# Jupyter 를 사용하면, 변수를 입력하고 난 뒤, 사용하고 싶은 함수에 대해 Tab 키로 불러와 입력하면 된다.

# 상위 데이터 
print(df.head(2))

# 하위 데이터
print(df.tail(2))

# 데이터프레임 Row Index
print(df.index)

# 데이터프레임 Column
print(df.columns)

# 데이터프레임 -> numpy 행렬
# 데이터프레임에 있던 행렬 값 타입이 일정하지 않으면 전부 Object 값으로 저장이 되는 것으로 인지하면 된다.
npy = df2.to_numpy()

print(npy)

# 평균, 표준편차, 최솟값, 사분할 정보 등은 describe() 함수를 사용해서 조회할 수 있다.
print(df.describe())

# T 는 (나이저 모건이 아니고) 전치 행렬로 만든다. (예를 들어 행렬을 각각 바꾸는 것이다.)
print(df.T)

# sort_index 는 0 이면 행을 기준, 1 이면 열을 기준으로 정렬한다. ascending 은 오름차순, 내림차순 일 것이다.
print(df.sort_index(axis=0, ascending=False))

# sort_values 는 열에 있는 값을 정렬하면, 이에 맞게 행을 정렬해주는 기능이다.
print(df.sort_values(by="C"))

# Selection 부터는 내일부터 공부 조이고~

import pandas as pd

df = pd.DataFrame({
    "a": [4,5,6,6],
    "b": [7,8,9,6],
    "c": [10,8,4,6]
}, index = [1, 2, 3, 4] # 인덱스가 row 번호.
)

print(df) # DataFrame (행렬)
print(df["a"]) # Series (벡터)
print(df[["a"]]) # DataFrame

# Subset
print(df["a"] > 5) # a 행렬 중 5 보다 큰 값을 가져온다.
print(df[["a", "b"]]) # 두 개 이상의 인덱스는 DataFrame 으로 가져와야 한다.

print(df["a"].value_counts()) # 데이터 빈도 수 추출
print(len(df)) # 데이터 ROW 개수
print(len(df.T)) # 데이터 COL 개수

print(df.sort_values("a", ascending=False)) # a 데이터를 기준으로 정렬. (정렬 순서만 변동. row 안의 데이터는 변경되지 않는다.)
 
df = df.drop(["c"], axis=1) # axis 기본 값이 0 이기 때문에 열을 기준으로 하려면, axis 값을 1 로 설정.
print(df)

# A 에 있는 값들을 기반으로 한 평균 값을 구하려면 아래와 같이 작성한다.
print(df.groupby("a")["b"].mean())
print(df.groupby("a")["b"].agg(["sum", "count"]))
print(df.groupby("a")["b"].describe())

# 엑셀이라 치면, VLOOKUP 같은 함수라 생각하면 되지 않을까?
print(pd.pivot_table(df, index="a", values="b", aggfunc="sum")) # 결과 값은 전체 평균으로 진행된다. (기본)

# plot 는 그래프를 그리기 위한 함수.
print(df.plot.area())

print(df["a"])
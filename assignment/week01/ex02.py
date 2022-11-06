import pandas as pd

# 호출
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/healthexp.csv")

# 피벗 테이블 생성
df_group = df.copy()

df_group = df_group.groupby(['Year', 'Country'])['Life_Expectancy'].mean().unstack()

df_group.sort_index(axis=0, ascending=True)

print('--- groupby 사용 ---')

print(df_group.loc[2011:])

# 피벗 테이블 생성
df_pivot = df.copy()

df_pivot = df_pivot.pivot_table(
    values = 'Life_Expectancy',
    index = 'Year',
    columns = 'Country',
    aggfunc = 'mean'
)

df_pivot.sort_index(axis=0, ascending=True)

print('--- pivot table 사용 ---')

print(df_pivot.loc[2011:])
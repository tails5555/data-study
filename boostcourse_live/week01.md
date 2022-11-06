# Data Science 1주차

## 주제

데이터 분석 환경 구성 및 준비하기

## 학습 정리

**Python**

- 프로그래밍 로직은 함수 외우기 등등이 다가 아니다. 작동하는 방식을 파악해야 한다.
- 공식문서를 주로 열람하는 것이 중요. 한국어로 나와 있긴 하다. 공부에 참조할 것.
- Python 기초 (Zen Of Python)
  - Python 의 사상. import this 명령어로 확인할 수 있다.
- 데이터 타입은 Number, String, Boolean 등.
- 인덱싱과 슬라이싱을 통해 원하는 데이터를 빠르게 가져올 수 있다.
- 리스트는 [], 딕셔너리는 { "" : "" }, 셋은 {}, 튜플은 ()
  - 튜플은 속도가 빠르고, immutable 하다.

**Pandas**

- Pandas Cheat Sheet -> 빅분기 분석 1번 문제까진 전부 풀 수 있을 것이다.
- ?? 으로 소스 코드를 볼 수 있다. ? 으로 도움말 볼 수 있다.
- DataFrame (2차원, 행렬), Series (1차원, 벡터)
- loc, iloc (DataFrame Slicing)
- at, iat (Single Value, Deprecated 가능성이...)
- Group By - agg(), transform(), filter() 사용
- Pivot (형태만 바꾸지 연산은 X), Pivot Table (연산도 가능하다)
- Stack (Melt 조이고, A, B 필드 -> 내부로 넣는 경우)
- Unstack (Unmelt 조이고, A, B 내부 -> A, B 필드로 넣는다.)
- 컬럼명들이 똑같으면 concat 을 사용할 수 있다.
- merge 는 DB 의 Join 이랑 같은 기능.
- 다양한 자료형을 불러올 수 있고, Plot 으로 그래프 조이고 할 수 있다.
- 절대경로 vs 상대경로 (웬만하면 상대경로를 사용할 수 있게 인덱싱을 잘 해 두자.)

# 데이터 사이언스

- Kaggle 노트북 따라해보기
- Kaggle Data Set 분석 및 경진대회 스터디
- 백엔드 이든 무엇이든 꾸준히 공부해보기
- 1일 1커밋 할 수 있으면 최대한...
- Product 개발 (직무 능력 향상)
- Researcher (석사 이상)



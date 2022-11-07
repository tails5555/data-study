import numpy as np

# 어떻게 사용되는지 정도는 파악해두고 갈 것.
ary = np.array([1, 2, 3])

print(ary)

ary2 = np.array(['mte', 'asd'])

print(ary2)

print(np.arange(5))

print(np.arange(2, 6, 0.3))

print(np.ones(5))

print(np.zeros(5))

print(np.full(5, 3))

print(np.ones((2, 3), dtype = 'int'))

print(np.zeros((2, 3), dtype = 'int'))

print(np.full((2, 3), 3))

print(np.identity(3))

# 아무래도 Pandas 데이터 타입에서 shape 로 받아오는게 여기서 비롯된 거 같다.
# 1차원에서 (1,) 로 나오는 이유? -> Python 에서 튜플 작성 시, ('asdf') == ('a', 's', 'd', 'f') 이렇기 때문... 그래서 ('asdf',) 이렇게 써두는 것이 좋다.
print(ary.shape)

print(np.ones((2, 3), dtype = 'int').shape)

# length 가 아님을 유의하라.
print(ary.size)

# Dimension Number 로 추정. 차원의 수를 반환한다.
print(ary.ndim)

# 음수여도... -3 까지만 된다. (길이가 3 인 경우) -1 을 쓰면 마지막 값을 가져온다.
print(ary[-1])

ary2d = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

# ary2d[1][1] 이 아님을 유의하라.
# 물론 음수 인덱스도 어느 차원을 가더라도 적용이 됨을 유의할 것.
print(ary2d[1,1])

# Java 의 substring 이랑 같은 원리 인덱스 책정이 된다.
print(ary[0:2])

# 위의 결과랑 똑같이 나온다. 어떤 의미인지 알 것이라 믿는다. (2차원도 마찬가지.)
print(ary[:2])

# 위의 결과랑 똑같이 나온다. 어떤 의미인지 알 것이라 믿는다. (2차원도 마찬가지.)
print(ary[-3:2])


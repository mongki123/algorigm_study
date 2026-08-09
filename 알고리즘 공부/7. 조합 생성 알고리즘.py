# 재귀 호출을 이용한 조합 생성 알고리즘 (Ex. 5개 중에서 3개)

# an[] : n개의 원소를 가지고 있는 리스트
# tr[] : 조합이 임시 저장될 r개의 크기의 리스트

def comb(n, r):
    if r == 0: print(tr)
    elif n < r : return
    else:
        tr[r - 1] = an[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)

an = ['A', 'B', 'C', 'D', 'E']
tr = [[0] for i in range(3)]
comb(5, 3)


# 아래는 파이썬 내장 라이브러리를 통한 조합 생성

import itertools
mylist = [1, 2, 3]

# 조합
result = itertools.combinations(mylist, r=2) # r 생략불가
print(list(result))

# 중복 조합
result = itertools.combinations_with_replacement(mylist, r=2) # r 생략불가
print(list(result))

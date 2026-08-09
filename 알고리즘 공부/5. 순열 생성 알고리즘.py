a = [1, 2, 3]

def perm(n, k):
    if k == n:
        print(a)
    else:
        for i in range(k, n):
            print(k,a)
            a[k], a[i] = a[i], a[k]
            perm(n, k + 1)
            a[k], a[i] = a[i], a[k]

perm(3, 0)


# 아래는 파이썬 내장 라이브러리를 통한 순열 생성

import itertools
mylist = [1, 2, 3]

# 순열
result = itertools.permutations(mylist) # (mylist, 3) r 생략시 기본값은 리스트 크기
print(list(result))

# 중복 순열
result = itertools.product(mylist, repeat=3)
print(list(result))
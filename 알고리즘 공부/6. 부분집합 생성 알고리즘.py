# 바이너리 기반 부분집합 생성 알고리즘

a = [1,2,3]
n = len(a)

for i in range(1 << n):
    print("십진수:", i, "이진수:", bin(i), ", result: ",end="")
    for j in range(n):
        
        if i & (1<<j): # i 의 j번째 비트가 1이면 j번쨰 원소 출력 (0100 = 0100 인지 and로 확인)
            print(a[j], end=" ")
    print()


# 아래는 슈퍼 간소화 버전

a = [1,2,3]

for i in range(1 << len(a)):
    print([a[j] for j in range(len(a)) if i & (1<<j)])
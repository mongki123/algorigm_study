# 현재 노드 자체가 공장이라는 것을 상기시켜야함.
T = int(input())

def Check(c, n, k, sum): # c = 선택 노드, n = 현재 노드, k = 최종 노드, sum = 총 생산비용
    global best
    
    if(best <= sum): # 가지치기
        return
    elif(n == k): # 전부 사용
        if best >= sum:
            best = sum
        return
    else:
        for i in range(k):
            if not c[i]:
                c[i] = True
                Check(c, n + 1, k, sum + arr[n][i])
                c[i] = False

for test_case in range(1 ,T + 1):
    N = int(input()) # 제품 수
    arr = [0 for i in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    best = float('inf')
    Check([False] *N, 0, N, 0)
    
    print(f"#{test_case} {best}")


# 아래 코드는 현재 노드를 인자로 받고 있지만 안사용하여
# 중첩 for 문이 만들어진 경우 (잘못 만듬, 시간초과 가능성 농후)

T = int(input())

def Check(c1, c2, n, k, sum): # c = 선택 노드, n = 현재 노드, k = 최종 노드, sum = 총 생산비용
    global best
    
    if(best <= sum): # 가지치기
        return
    elif(n == k): # 전부 사용
        best = sum
    else:
        for c_1 in range(len(c1)): # 공장 선택문
            if c1[c_1] == False: # 현재 노드가 미선택일시
                for c_2 in range(len(c1)): # 제품 선택문
                    if c2[c_2] == False: # 현재 노드가 미선택일시
                        c1[c_1], c2[c_2] = True, True # 공장 사용
                        Check(c1, c2, n + 1, k, sum + arr[c_1][c_2])
                        c1[c_1], c2[c_2] = False, False # 백트레킹

for test_case in range(1 ,T + 1):
    N = int(input()) # 제품 수
    arr = [0 for i in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    best = float('inf')
    Check([False] *N, [False] *N, 0, N, 0)
    
    print(f"#{test_case} {best}")

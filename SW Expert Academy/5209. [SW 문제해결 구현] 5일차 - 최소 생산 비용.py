T = int(input())

def Check(c, n, k, sum): # c = 선택 노드, n = 현재 노드, k = 최종 노드, sum = 총 생산비용
    global best
    
    if(best <= sum):
        return
    elif(n == k):
        best = sum
    else:
        # 여기에 함수 제작
        for i in arr:
            if c[n] == False: # 현재 노드가 미선택일시
                c[n] = True
                for j in i:
                    sum += j
                    Check(c, n + 1, k, sum)
                    sum -= j # 백트레킹
                c[n] = False # 백트레킹

for test_case in range(1 ,T + 1):

    N = int(input()) # 제품 수
    arr = [0 for i in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    best = float('inf')
    Check([False] * N, 0, N, 0)
    
    print(f"#{test_case} {best}")


    # 이거 choice 부분만 수정하면 될 듯 ㄹㅇ 최적의 것만 가져오고 있음.
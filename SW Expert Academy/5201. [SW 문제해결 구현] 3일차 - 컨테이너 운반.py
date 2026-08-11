# 탐욕적으로 풀어봤음. 그냥 단순히 높은 화물이 높은 물건을 가져간다는 개념.

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # 컨테이너 수, 트럭 수
    nWeis= sorted(map(int, input().split()),reverse=1) # N개의 화물의 무게
    mWeis = sorted(map(int, input().split()),reverse=1) # M개의 트럭의 적재용량

    truckSum = 0
    for i in range(M):
        for j in range(N):
            if mWeis[i] >= nWeis[j]:
                truckSum += nWeis[j]
                nWeis[j] = float('inf')
                break
    
    print(f"#{test_case} {truckSum}")
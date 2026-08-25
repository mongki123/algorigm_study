T = int(input())

def batteryCheck(choice, n, k): # choice = 선택 결과, n = 현재 정류장, k = 종착점
    global best
    
    if(best <= len(choice)):
        return
    elif(n >= k):
        best = len(choice)
    else:
        for i in range(1, batterys[n-1] + 1):
            if n == 1: # 출발점, 교체 안함 = choice 추가 X
                batteryCheck(choice, n + i, k)
            else:
                choice.append(n)
                batteryCheck(choice, n + i, k)
                choice.pop()

for test_case in range(1, T + 1):

    inputTemp = list(map(int, input().split()))
    N = inputTemp[0] # 정류장 수
    batterys = inputTemp[1:] # 정류장 별 배터리 용량

    best = float('inf')
    batteryCheck([], 1, N)
    print(f"#{test_case} {best}")



###########################################################
# 아래는 제미나이가 cnt 사용하여 푼 것.
# 동전 거스름돈이였으면 위 방식이 맞지만 이건 단순 카운트라
# 쓸모 없는 메모리 사용이 될 수 있음. 그러므로 아래 방식 선호

def batteryCheck(n, cnt, k):
    global best
    
    # 이미 최소 횟수를 넘었거나 같으면 더 볼 필요 없음 (가지치기)
    if best <= cnt:
        return
    
    # 종점에 도착하거나 넘었을 때
    if n >= k:
        best = min(best, cnt)
        return
        
    # 현재 정류장에서 배터리 용량만큼 반복 (큰 값부터 탐색하면 가지치기 효율이 더 좋아집니다)
    battery_power = batterys[n-1]
    for i in range(battery_power, 0, -1):
        # 출발점(n==1)에서 출발할 때는 교체 횟수(cnt)를 늘리지 않음
        next_cnt = cnt if n == 1 else cnt + 1
        batteryCheck(n + i, next_cnt, k)

T = int(input())
for test_case in range(1, T + 1):
    inputTemp = list(map(int, input().split()))
    N = inputTemp[0] 
    batterys = inputTemp[1:] 

    best = float('inf')
    batteryCheck(1, 0, N)
    print(f"#{test_case} {best}")
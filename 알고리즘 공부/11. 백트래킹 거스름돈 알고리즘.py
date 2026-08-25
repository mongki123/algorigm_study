# coin[] : 동전의 금액을 저장
# choice[] : 선택한 동전들의 집합
# best : 거스름돈에 대한 최소 동전 개수

def CoinChange(choice, N, money):
    global best
    if best <= N:
        return
    elif money == 0:
        best = N
    else:
        for i in range(len(coin)):
            if money - coin[i] >= 0:
                choice[N] = coin[i]
                CoinChange(choice, N + 1, money - coin[i])

best = float('inf')
coin = [10,50,100,400,500]
choice = [0 for i in range(99)]
CoinChange(choice, 0, 800)
print(best)

######################################################################

# 아래는 list append, pop을 활용한 방법, 초기 choice 값 선언 필요 없음.
def CoinChange(choice, N, money):
    global best
    if best <= len(choice):
        return
    elif money == 0:
        if len(choice) < best:
            best = len(choice)
            # 최적의 조합을 저장하고 싶다면 여기서 전역 변수에 복사
    else:
        for i in range(len(coin) - 1, -1, -1):  # 큰 동전부터 탐색 (최적화)
            if money - coin[i] >= 0:
                choice.append(coin[i])          # 선택하고 추가
                CoinChange(choice, N + 1, money - coin[i])
                choice.pop()                    # 돌아와서 취소 (백트래킹)

best = float('inf')
coin = [10, 50, 100, 400, 500]
CoinChange([], 0, 800)
print(best)
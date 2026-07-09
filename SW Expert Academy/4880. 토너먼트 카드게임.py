"""
거의 다 왔는데 결국 Grok 도움 받음... 재귀 함수 공부 more 필요
"""

def Check(arr, start, end): # start = 첫 번째 플레이어, end = 두 번째 플레이어
    if end - start < 1 : # 부전승
        return
    if end - start == 1 : # 결투
        duel(arr, start, end)
        return

    mid = (start + end) // 2
    Check(arr, start, mid)
    Check(arr, mid + 1, end)

    left_winner = find_winner(arr, start, mid)
    right_winner = find_winner(arr, mid + 1, end)

    if left_winner != None and right_winner != None:
        duel(arr, left_winner, right_winner)

def duel(arr, left, right):
    if(arr[left] == 1 and arr[right] == 3):
        arr[right] = 0
    elif(arr[left] == 2 and arr[right] == 1):
        arr[right] = 0
    elif(arr[left] == 3 and arr[right] == 2):
        arr[right] = 0
    elif(arr[left] == arr[right]):
        arr[right] = 0
    else:
        arr[left] = 0

def find_winner(arr, start, end):
    for i in range(start, end + 1):
        if arr[i] != 0:
            return i
    return None

T = int(input())
for t in range(1, T + 1):
    num = int(input())
    arr = list(map(int, input().split()))
    Check(arr, 0, num-1)
    for i in range(num):
        if arr[i] != 0:
            print(f"#{t} {i+1}")
            break
# 중복 X 순열로 풀어보자!
T = int(input())

def Check(arr, i, j, sum):
    global result
    aLen = len(arr)

    # 1. 범위를 벗어난 경우
    if aLen <= i or aLen <= j:
        return
    # 2. 최솟값 오버 확인
    if sum >= result:
        return
    # 3. 도착점에 도달한 경우
    if aLen -1 == i and aLen -1 == j:
        sum += arr[i][j]
        if sum < result:
            result = sum
        return

    sum += arr[i][j]
    Check(arr, i + 1, j, sum)
    Check(arr, i, j + 1, sum)

for test_case in range(1, T + 1):
    aLen = int(input())
    arr = []
    for i in range(aLen):
        arr.append(list(map(int, input().split())))

    result = float('inf')
    Check(arr, 0, 0, 0)

    print(f"#{test_case} {result}")
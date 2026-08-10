# 중복 X 순열로 풀어보자!
T = int(input())


def Check(arr, aLen, n, lo, sum):
    global result
    if(result <= sum):
        return
    if((aLen - 1) <= n):
        if result > sum:
            print(f"{n}: {lo+1} -> {1}, sum: {sum}, result: {result}")
            result = sum + arr[lo][0]
        return
    for i in range(n, aLen):
        if i == n: continue
        sum += arr[lo][i]
        print(f"{n}: {lo+1} -> {i+1}, sum: {sum}, result: {result}")
        Check(arr, aLen, n + 1, i, sum)

for test_case in range(1, T + 1):
    aLen = int(input())
    arr = [list(map(int, input().split())) for _ in range(aLen)]
    result = float('inf')
    Check(arr, aLen, 0, 0, 0)
    
    print(f"#{test_case} {result}")
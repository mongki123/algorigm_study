# 백트래킹으로 푸는 중.

T = int(input())

def Check(n, k):
    global result
    
    sum = int("".join(map(str, arr)))
    if(result >= sum):
        return
    elif(n == k):
        if(result < sum):
            result = sum
        return
    else:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if(i != j):
                    arr[i], arr[j] = arr[j], arr[i]
                    Check(n + 1, k)
                    arr[i], arr[j] = arr[j], arr[i]

for test_case in range(1, T + 1):

    temp, N = map(int,input().split())
    arr = list(map(int, str(temp)))

    result = 0
    Check(0, N)
        
    print(f"#{test_case} {result}")
T = int(input())
 
 
 
def Check(arr, start, end):
 
    global sum
     
    if start >= end:
        return
         
    maxInt = max(arr[start:(end + 1)])
     
    i = start
    while(arr[i] != maxInt):
        if arr[i] < maxInt:
            sum = sum + (maxInt - arr[i])
            i = i + 1
 
    if start == i:
        i += 1
 
    Check(arr, i, end)
 
 
 
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    sum = 0
    Check(arr, 0, N - 1)
 
    print(f"#{test_case} {sum}")
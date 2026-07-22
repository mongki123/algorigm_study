# BFS로 풀기!

T = int(input())

def Check(arr, start, result, sum):

    sum += start
    tempArr = arr.copy()

    if sum not in result:
        result.append(sum)

    tempArr.remove(start)
    if len(tempArr) <= 0:
        tempArr = arr.copy()
        return
        
    for i in arr:
        print(arr)
        Check(tempArr, i, result, sum)
    


for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = [0]
    for i in arr:
        if i not in result:
            result.append(i)
            
    Check(arr, arr[0], result, 0)

    print(f"#{test_case} {len(result)}")
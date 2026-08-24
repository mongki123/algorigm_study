T = int(input())

def Check(arr, start, end, key, isRoof):
 
    if(start > end or start < 0):
        return False
    
    middle = (start + end) // 2

    if(key == arr[middle]):
        return True
    elif(key < arr[middle]):
        if(isRoof == "Left"):
            return False
        return Check(arr, start, middle - 1, key, "Left")
    elif(key > arr[middle]):
        if(isRoof == "Right"):
            return False
        return Check(arr, middle + 1, end, key, "Right")
    


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arrN = sorted(list(map(int, input().split())))
    arrM = list(map(int, input().split()))
    result = 0

    for m in arrM:
        if Check(arrN, 0, N-1, m, ""):
            result += 1
        
    print(f"#{test_case} {result}")
T = int(input())

def Check(arr, start, change):
    
    if(change <= 0):
        return

    aLen = len(arr)
    num2 = aLen
    max = start
    choice = change
    
    for i in range(start, aLen):    
        num2 -= 1
        if arr[max] < arr[num2]:
            max = num2
            choice = change
        elif(arr[max] == arr[num2]):
            if(choice > 1):
                choice -= 1
                max = num2
            
    if(arr[start] <= arr[max]):
        temp = arr[start]
        arr[start] = arr[max]
        arr[max] = temp
        change -= 1
        Check(arr, start + 1, change)
    
    else:
        print(arr)
        Check(arr, start + 1, change)
    
    
for test_case in range(1, T + 1):
    
    arr, change = map(int, input().split())
    arr = list(map(int, str(arr)))
    Check(arr, 0, change)
    
    print(f"#{test_case}", end = ' ')
    for data in arr:
        print(data,end='')
    print()
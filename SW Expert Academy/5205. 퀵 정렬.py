T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def quickSort(arr, start, end):
    
    if(start >= end):
        return

    key = start
    i = start + 1
    j = end

    while(i <= j):

        while(arr[i] <= arr[key] and i < end):
            i += 1
        while(arr[j] >= arr[key] and j > start):
            j -= 1
            
        if(i >= j):
            temp = arr[key]
            arr[key] = arr[j]
            arr[j] = temp
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            
    quickSort(arr, start, j - 1)
    quickSort(arr, j + 1, end)
            
        

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    number = int(input())
    arr = list(map(int, input().split()))
    quickSort(arr, 0, number - 1)
    print(f"#{test_case} {arr[int(number/2)]}")
    # ///////////////////////////////////////////////////////////////////////////////////

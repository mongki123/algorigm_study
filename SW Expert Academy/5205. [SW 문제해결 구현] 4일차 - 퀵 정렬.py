T = int(input())

def QuikSort(arr, start, end):

    if(start >= end):
        return
        
    pibot = start
    i = start + 1
    j = end
    
    while(i <= j):
        while(i <= end and arr[i] <= arr[pibot]):
            i += 1
        while(j > start and arr[j] >= arr[pibot]):
            j -= 1
        if(i >= j):
            arr[j], arr[pibot] = arr[pibot], arr[j]
        else:
            arr[i], arr[j] = arr[j], arr[i]   

    QuikSort(arr, start, j - 1)
    QuikSort(arr, j + 1, end)


for test_case in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input().split()))

    QuikSort(arr, 0, len(arr) - 1)

    print(f"#{test_case} {arr[N//2]}")
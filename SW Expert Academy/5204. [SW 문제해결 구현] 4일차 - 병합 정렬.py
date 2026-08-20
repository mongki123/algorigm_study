T = int(input())

def Merge(left, right):
    result = []
    i, j = 0, 0
    while (len(left) > i and len(right) > j):
        if(left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if(len(left) > i):
        result.extend(left[i:])
    if(len(right) > j):
        result.extend(right[j:])

    return result
        

def Sort(arr):
    # global count
    
    if(len(arr) <= 1):
        return arr, 0

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left, count_le = Sort(left)
    right, count_ri = Sort(right)

    count = count_le + count_ri

    if(left[-1] > right[-1]):
        count +=1
    
    return Merge(left, right), count

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr, count = Sort(arr)
    print(f"#{test_case} {arr[len(arr)//2]} {count}")
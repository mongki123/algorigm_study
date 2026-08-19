T = int(input())

def Merge(left, right):
    result = []

    print(right)
    while (len(left) > 0 and len(right) > 0):
        if(left[-1] >= right[-1]):
            result.append(left.pop(-1))
        else:
            result.append(right.pop(-1))
    if(len(left) > 0):
        result.extend(left)
    if(len(right) > 0):
        result.extend(right)

    result = list(reversed(result))
    
    return result
        

def Sort(arr):
    if(len(arr) <= 1):
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = Sort(left)
    right = Sort(right)

    return Merge(left, right)

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr = Sort(arr)

    print(f"#{test_case} {arr}")
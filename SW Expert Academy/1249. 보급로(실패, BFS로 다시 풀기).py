T = int(input())

def Check(arr, i, j, sum, fix):
    global result

    if(sum >= result):
        return
    if(i == len(arr) - 1 and j == len(arr) - 1):
        result = sum
        print(result)
        return
        
    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for nDir in direction:
        if(i + nDir[0] < len(arr) - 1 and i + nDir[0] >= 0 and j + nDir[1] < len(arr) - 1 and j + nDir[1] >= 0):
            if((i + nDir[0], j + nDir[1]) not in fix):
                Check(arr, i + nDir[0], j + nDir[1], sum + arr[i + nDir[0]][j + nDir[1]], fix.append((i + nDir[0],j + nDir[1])))
    

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[] for i in range(N)]
    for i in range(N):
        for j in input():
            arr[i].append(int(j))

    result = float('inf')
    Check(arr, 0, 0, 0, [])

    result = 0
    print(f"#{test_case} {result}")
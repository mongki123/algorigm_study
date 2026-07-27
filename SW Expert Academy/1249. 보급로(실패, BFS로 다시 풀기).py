T = int(input())

def Check(arr, x, y, dire):

    N = len(arr[0])
    global resultSum
    
    if x >= (N - 1) and y >= (N - 1):
        return

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)] #오, 아, 위, 왼
    result = {'0' : 999, '1' : 999, '2' : 999, '3' : 999}
    for i in range(len(directions)):
        
        if (dire == 0 and i == 3) or (dire == 1 and i == 2) or (dire == 2 and i ==1) or (dire == 3 and i == 0): #되돌아가기 방지용
            continue
        if (x + directions[i][0]) < N and (x + directions[i][0]) >= 0 and (y + directions[i][1]) < N and (y + directions[i][1]) >= 0:
            result[str(i)] = arr[x + directions[i][0]][y + directions[i][1]] 
    rD = int(min(result, key=result.get))
    resultSum += result[str(rD)]
    Check(arr, x + directions[rD][0], y + directions[rD][1], rD)    
    

for test_case in range(1, T + 1):
    N = int(input())
    arr = []

    for i in range(N):
        arr.append(list(map(int, str(input()))))

    resultSum = 0
    Check(arr, 0, 0, -1)

    print(f"#{test_case} {resultSum}")



    
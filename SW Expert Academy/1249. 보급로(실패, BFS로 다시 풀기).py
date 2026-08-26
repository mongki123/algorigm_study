# 백트래킹(DFS) 를 구현하여 풀긴 하였으나 시관초과 뜬 코드
# 이건 DFS 말고 다른 알고리즘으로 해야한다고...

T = int(input())

def Check(boolArray, i, j, sum):
    global result

    if(sum >= result):
        return
      
    elif(i == N - 1 and j == N - 1):
        if result >= sum:
            result = sum
        return

    else:
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
        for nDir in direction:
            if(i + nDir[0] < N and i + nDir[0] >= 0 and j + nDir[1] < N and j + nDir[1] >= 0):
                if(not boolArray[i + nDir[0]][j + nDir[1]]):
                    boolArray[i][j] = True
                    Check(boolArray, i + nDir[0], j + nDir[1], sum + arr[i + nDir[0]][j + nDir[1]])
                    boolArray[i][j] = False

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[] for i in range(N)]
    for i in range(N):
        for j in input():
            arr[i].append(int(j))

    result = float('inf')
    temp = [[False] * N for i in range(N)]
    Check(temp, 0, 0, 0)
    print(f"#{test_case} {result}")
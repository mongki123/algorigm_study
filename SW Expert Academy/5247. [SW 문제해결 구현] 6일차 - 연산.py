# visited 와 queue 구조를 확실히 이해할 것.
# from collections import deque <- 이건 기억해두자.
# popleft를 했을때 시간 복잡도가 N 이나 차이가 난다.

from collections import deque

def RunBFS(start, end):
    visited = [False] * 1000001
    queue = deque([(start, 0)])
    visited[start] = True
    
    while queue:
        current, count = queue.popleft()

        if(current == end):
            return count
        
        cal = [current + 1, current - 1, current * 2, current - 10]
        
        for next_value in cal:
            if(1 <= next_value <= 1000000 and not visited[next_value]):
                visited[next_value] = True
                queue.append((next_value, count + 1))




T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    result = RunBFS(N, M)
    print(f"#{test_case} {result}")
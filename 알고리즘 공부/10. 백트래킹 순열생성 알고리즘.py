def permutation(k, n, order, visited):
    if k == n:
        print(order)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True      # i번째 원소 사용 체크
            order[k] = i           # 현재 자리에 i 넣기
            permutation(k + 1, n, order, visited)
            visited[i] = False     # 원상복구 (Backtracking)

n = 4
permutation(0, n, [0] * n, [False] * n)
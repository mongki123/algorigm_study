T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    Narr = [[i] for i in range(1, N + 1)]
    Mchoi = list(map(int, input().split()))

    for i in range(M * 2):
        if i % 2 == 0:
            left = Mchoi[i]-1
            right = Mchoi[i+1]-1
            if left > right:
                left, right = right, left

            if Narr[left][0] == left + 1:
                Narr[left].append(right + 1)
                Narr[right] = [left + 1]
            else:
                Narr[Narr[left][0]-1].append(right + 1)
                Narr[right] = [Narr[left][0]]
                
    for i in range(N-1,0,-1):
        if i >= len(Narr):
            break
        if(len(Narr[i]) == 1 and Narr[i][0] != i + 1):
            Narr.pop(i)
            
    result = len(Narr)
        
    print(f"#{test_case} {result}")
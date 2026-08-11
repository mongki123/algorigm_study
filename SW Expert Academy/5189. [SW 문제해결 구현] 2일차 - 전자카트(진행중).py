import itertools

T = int(input())

for test_case in range(1, T + 1):
    aLen = [i for i in range(1, int(input())+1)] # 순열 생성 [1, 2, 3]
    aPers = list(itertools.permutations(aLen[1:]))
    arr = [list(map(int, input().split())) for _ in range(len(aLen))]
    result = float('inf')
    
    for aPer in aPers:
        sum = arr[0][1]
        for num in aPer:
            if num + 1 >= len(aPer):
                sum += arr[num][0]
            else:
                sum += arr[num][num + 1]
            if sum > result:
                break
        if result < sum:
            result = sum
    
    print(f"#{test_case} {result}")


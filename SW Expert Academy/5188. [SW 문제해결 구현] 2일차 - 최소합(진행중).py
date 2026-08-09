# 중복 X 순열로 풀어보자!
T = int(input())
    
for test_case in range(1, T + 1):
    aLen = int(input())
    arr = []
    for i in range(aLen):
        arr.append(list(map(int, input().split())))

    ### 여기다가 적자!
    
    print(f"#{test_case} {result}")
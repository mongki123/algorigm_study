T = int(input())

for test_case in range(1, T + 1):

    N, number = map(str, input().split())

    result = ""
    for i in range(int(N)):        
        if number[i] == 'A': num = 10
        elif number[i] == 'B': num = 11
        elif number[i] == 'C': num = 12
        elif number[i] == 'D': num = 13
        elif number[i] == 'E': num = 14
        elif number[i] == 'F': num = 15
        else: num = int(number[i])
        temp = ""
        for j in range(4):
            exNum = num % 2
            num = num // 2
            temp = str(exNum) + temp
        result = result + temp
    print(f"#{test_case} {result}")
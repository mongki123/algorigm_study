T = int(input())

for test_case in range(1, T + 1):

    number = float(input())

    result = ""
    
    sum = 0.0000000000000
    for i in range(-1, -14, -1):
        if(number >= sum + 2 ** i):
            result = result + '1'
            sum = sum + 2 ** i
        else:
            result = result + '0'
        
        if(number == sum):
            print(f"#{test_case} {result}")
            break
        elif(number < sum):
            print(f"#{test_case} overflow")
            break
        elif(i == -13):
            print(f"#{test_case} overflow")


# 위 코드가 내가 푼 코드
# 직접 비트 가중치를 빼가며 구현해보려고 하신 시도는 좋으나 좋은 코드는 아님.

# 아래 코드가 재미나이가 푼 코드
# 소수에 2를 곱하여 진수변환 <- 이거 개신박하네 신기하당

T = int(input())

for test_case in range(1, T + 1):
    number = float(input())
    result = ""
    cnt = 0
    
    while number > 0:
        number *= 2
        result += str(int(number))
        number -= int(number) # 소수점 아래만 남김
        cnt += 1
        
        if cnt > 12: # 12자리를 초과하면 overflow
            break
            
    if cnt > 12:
        print(f"#{test_case} overflow")
    else:
        print(f"#{test_case} {result}")
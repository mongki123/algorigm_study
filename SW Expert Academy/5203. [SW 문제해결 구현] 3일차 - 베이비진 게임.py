# 풀긴 하였으나 최적화 필요해보임.

T = int(input())

def Check(p1, p2):

    #p1
    counter = 0
    for i in range(len(p1)):
        if(p1[i] >= 1):
            if(p1[i] >= 3):
                return 1
            else:
                if(counter >= 2):
                    return 1
                elif(i <= 8):
                    if(p1[i + 1] >= 1):
                        counter += 1
                    else:
                        counter = 0      
                    
    #p2
    counter = 0
    for i in range(len(p1)):
        if(p2[i] >= 1):
            if(p2[i] >= 3):
                return 2
            else:
                if(counter >= 2):
                    return 2
                elif(i <= 8):
                    if(p2[i + 1] >= 1):
                        counter += 1
                    else:
                        counter = 0

    #무승부
    return 0
    

for test_case in range(1, T + 1):
    
    cards = list(map(int, input().split()))

    p1 = [0 for _ in range(10)]
    p2 = [0 for _ in range(10)]
    
    for i in range(len(cards)):
        # card 추가
        if(i % 2 == 0):
            p1[cards[i]] += 1
        else:
            p2[cards[i]] += 1

        #print(p1)
        #print(p2)

        # 비교 
        if(i >= 5): # 카드가 각각 3장 이상일 때
            result = Check(p1, p2)
            if(result >= 1):
                break

    print(f"#{test_case} {result}")
"""
생각해보니 반 나누고 그걸 재귀로 들어가서 가위바위보 하면
될 듯 함. 이걸로 해보자.

"""

T = int(input())


def Check(students, number):

    victory = []
    Player1 = 0
    Player2 = 0
    Case = 0
    Case2 = 0
    
    for i in range(0, number, 2):
    
        for Case in range(number):
            if(Case < number and students[Case] != 0):
                Player1 = students[Case]
        for Case2 in range(Case, number):
            if(Case2 < number and students[Case2] != 0):
                Player2 = students[Case2]
    
        if(Player1 != 0 and Player2 != 0):
            if(Player1 == 1 and Player2 == 3): # 가위 vs 보
                students[Case2] = 0
            elif(Player1 == 2 and Player2 == 1): # 바위 vs 가위
                students[Case2] = 0
            elif(Player1 == 3 and Player2 == 2): # 보 vs 주먹
                students[Case2] = 0
            elif(Player1 == Player2): # 비긴 경우
                students[Case2] = 0
            else:
                students[Case] = 0 # 진 경우

        elif(Player1 == 0 or Player2 == 0): # 부전승 또는 우승
            if(sum(students) == Player1 or sum(students) == Player2): # 우승
                print(students[Player1])
                return

    Check(students, number)
    

for test_case in range(1, T + 1):
    number = int(input())
    students = list(map(int, input().split()))

    print(f"#{test_case} ", end ="")
    Check(students, number - 1)
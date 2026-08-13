T = int(input())

for test_case in range(1, T + 1):

    timeDic = {} # 시작 시간 / 끝나는 시간
    N = int(input())
    for i in range(N):
        timeTemp = input().split() # 시작 시간 / 끝나는 시간
        if int(timeTemp[0]) in timeDic.keys():
            if int(timeDic[int(timeTemp[0])]) > int(timeTemp[1]):
                timeDic[int(timeTemp[0])] = timeTemp[1]
        else:
            timeDic[int(timeTemp[0])] = timeTemp[1]

    # 끝난 시간 오름차순 정렬
    timeDic = sorted(timeDic.items())
    
    timeCount = 0
    localTime = 0
    prevTime = 0
    for i in range(len(timeDic)):
        if int(timeDic[i][0]) >= localTime and int(timeDic[i][1]) >= localTime:
            prevTime = int(timeDic[i][0])
            localTime = int(timeDic[i][1])
            timeCount += 1
        elif int(timeDic[i][0]) >= prevTime and int(timeDic[i][1]) < localTime:
            prevTime = int(timeDic[i][0])
            localTime = int(timeDic[i][1])
        
    
    print(f"#{test_case} {timeCount}")



# 이게 lambda 를 몰라서 개 어렵게 되어있는데. lambda 쓰면 개편해짐.
"""
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    dock = []
    
    for _ in range(N):
        start, end = map(int, input().split())
        dock.append((start, end))
    
    # 1. 끝나는 시간을 기준으로 오름차순 정렬, 끝이 같다면 시작 시간 기준 오름차순 정렬
    dock.sort(key=lambda x: (x[1], x[0]))
    
    timeCount = 0
    end_time = 0  # 직전 작업이 끝난 시간
    
    for start, end in dock:
        # 현재 작업의 시작 시간이 이전 작업의 종료 시간보다 크거나 같으면 선택
        if start >= end_time:
            end_time = end
            timeCount += 1
            
    print(f"#{test_case} {timeCount}")
"""
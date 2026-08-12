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
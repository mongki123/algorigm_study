T = int(input())

for test_case in range(1, T + 1):
    arr = list(input())

    dic = {'N' : 0, 'S' : 0, 'E' : 0, 'W' : 0}
        
    for A in arr:
        if dic[A] == 0 : dic[A] = 1

    if (dic['N'] + dic['S']) % 2 == 0 and (dic['E'] + dic['W']) % 2 == 0:
        print("Yes")
    else:
        print("No")
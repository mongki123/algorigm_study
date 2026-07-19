T = int(input())

def Paint(arr, i, j, way):
    global count, num

    if(count >= (num ** 2)):
        arr[i][j] = count
        return
    
    if(way == "right"):
        if (j + 1) >= num: way = "down"
        elif arr[i][j + 1] != 0: way = "down"
    elif(way == "down"):
        if (i + 1) >= num: way = "left"
        elif arr[i + 1][j] != 0: way = "left"
    elif(way == "left"):
        if (j - 1) < 0: way = "up"
        elif arr[i][j - 1] != 0: way = "up"
    elif(way == "up"):
        if (i - 1) < 0: way = "right"
        elif arr[i - 1][j] != 0: way = "right"

    arr[i][j] = count
    count += 1
    
    if way == "right": j += 1
    elif way == "down": i += 1
    elif way == "left": j -= 1
    elif way == "up": i -= 1
        
    Paint(arr, i, j, way)
        
        


for test_case in range(1, T + 1):
    num = int(input())
    count = 1
    arr = [[0 for _ in range(num)] for _ in range(num)]
    
    Paint(arr, 0, 0, "right")

    print(f"#{test_case}")
    for i in range(num):
        for j in range(num):
            print(arr[i][j], end=" ")
        print("")
            


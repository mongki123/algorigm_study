T = int(input())
for test_case in range(1,T + 1):
    N = int(input())

    temp = input()
    stack = []
    point = 0
    
    for i in range(N):
        stack.append(temp[i])
        
        if(len(stack) >= 3):
            if(stack[len(stack) - 1] == 'x' and stack[len(stack) - 2] == 'o' and stack[len(stack) - 3] == 'f'):
                stack.pop()
                stack.pop()
                stack.pop()
                
    print(len(stack))
            
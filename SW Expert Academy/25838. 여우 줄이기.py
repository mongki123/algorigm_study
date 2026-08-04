# 스택 문제, List를 활용하여 스택처럼 사용.
# 스택으로 사용하기 때문에 fox 순으로 감지하는게 아닌 "xof 순으로 감지"

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
            

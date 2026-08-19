def Recursive_Power(C,n):
    if n == 1:
        return C
    if n % 2 == 0: # even
        y = Recursive_Power(C, n/2)
        return y * y
    else:
        y = Recursive_Power(C, (n-1)/2)
        return y * y * C

print(Recursive_Power(2, 4))
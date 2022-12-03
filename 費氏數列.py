a = int(input())

F0 = 0
F1 = 1

def F(n):
    if n == 0:
        return 0
        
    elif n == 1:
        return 1
    
    else:
        return F(n - 1) + F(n - 2)
    
print(F(a))
print()
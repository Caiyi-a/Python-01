a = input()

def al(s):
    b = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    c = list(range(10, 36))
    
    for i in range(len(b)):
        if s[0] == b[i]:
            X = str(c[i])
    
    X1 = X[0]
    X2 = X[1]
    
    return X1, X2

def num(s):
    a = 0
    b = 8
    for i in range(len(s) - 1):
        a += b * int(s[i])
        b -= 1
        
    a += int(s[-1])
    
    return a

def IC(s):
    X1, X2 = al(s[0])
    
    a = num(s[1:])
    
    ans = int(X1) + 9 * int(X2) + a
    
    if ans % 10 == 0:
        return 'CORRECT!!!\n'
    
    else:
        return 'WRONG!!!\n'

print(IC(a))
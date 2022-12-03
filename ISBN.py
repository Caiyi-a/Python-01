a = input().split()

def num(n):
    for i in range(len(n)):
        if n[i] == 'X':
            n[i] = '10'
            
    return n
        
def ac(n):
    c = []
    d = 0
    
    for i in range(len(n)):
        d += int(num(n)[i])
        
        c.append(d)
        
    return c

def check(n):
    if ac(ac(n))[-1] % 11 == 0:
        return True
    
    else:
        return False

if check(a) == True:
    print('YES')
    
else:
    print('NO')
    
print()
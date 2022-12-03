def fac(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
        
    return a

def C(m, n):
    b = fac(m) // (fac(n) * fac(m - n))
    
    return b

m, n = map(int, input().split())
print(C(m, n))
n = int(input())

def f(n):
    a = 0
    if n == 1:
        a = n + 1
        
    elif n > 1:
        a = f(n - 1) + f(n // 2)
        
    return a

print(f(n))
a = int(input())

def v(n):
    if n == 0:
        return 0
    
    else:
        return 1 + v(n // 10)
    
print(v(a))
print()
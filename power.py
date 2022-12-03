a, b = map(int, input().split())

def power(a, n):
    if n == 1:
        ans = a
        
    else:
        ans = a * power(a, n - 1)
    
    return ans

print(power(a, b))
print()
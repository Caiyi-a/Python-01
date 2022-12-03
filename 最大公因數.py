a = list(map(int, input().split()))

b = max(a)
c = min(a)

def hcf(m, n):
    for i in range(1, min(a) + 1):
        if b % i == 0 and c % i == 0:
            hcf = i
            
    return hcf

print(hcf(b, c))
print()
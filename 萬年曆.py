y, m = map(int, input().split())

def leap_year(n):
    flag = False
    if n % 400 == 0:
        flag = True
        
    elif n % 4 == 0 and n % 100 != 0:
        flag = True
        
    return flag

def month_day(n, m):
    a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if leap_year(n) == True:
        a[1] = 29
        
    return a[m - 1]

def day_num(n, m):
    d = 0
    
    for i in range(1, n):
        if leap_year(i) == True:
            d += 366
            
        else:
            d += 365
            
    for i in range(1, m):
        d += month_day(n, i)
        
    return d

def week(n, m):
    a = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    
    return a[(day_num(n, m) + 1) % 7]

a = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i in a:
    print(i, end = '\t')
    
print()

b = week(y, m)
d = []
e = 1

for i in range(len(a)):
    if b == a[i]:
        c = len(a) - i - 1
        
for i in range(1, month_day(y, m) + 1):
    if i == e + c:
        d.append(i)
        e += 7

for i in a:
    if b == i:
        print('{:>3}'.format(1), end = '\t')
        break
        
    else:
        print(' ', end = '\t')
        
for i in range(2, month_day(y, m) + 1):
    if i in d:
        print('{:>3}'.format(i))
        
    else:
        print('{:>3}'.format(i), end = '\t')
        
print()
print()
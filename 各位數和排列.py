a = int(input())
b = input()

def sum(n):
    c = n.split()
    d = 0
    e = []
    f = []
    g = []
    h = []
    
    for i in c:
        d = 0
        for j in i:
            d += int(j)
        
        e.append([d, int(i)])
        f.append(d)
        
    f.sort()
    
    for i in range(len(e) - 1):
        for j in range(i + 1, len(e)):
            if e[i][0] == e[j][0]:
                x = e[i][1]
                e[i][1] = [x, int(e[j][1])]
                e[i][1].sort()
                e[j] = [0, 0]
        
    for i in range(len(f)):
        if not f[i] in g:
            g.append(f[i])
    
    for i in g:
        for j in e:
            if i == j[0]:
                h.append(j[1])
            
    return h

c = sum(b)

for i in c:
    if type(i) == list:
        for j in i:
            print(j, end = '\t')
            
    else:
        print(i, end = '\t')
        
print()
print()
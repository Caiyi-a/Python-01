def sep_num(n):
    a = ''
    for i in range(len(n)):
        if i != len(n):
            a += n[i] + ' '
            
        else:
            a += n[i] + '\n'
        
    return a

n = input()
print(sep_num(n))
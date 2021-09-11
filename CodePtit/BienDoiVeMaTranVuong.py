n , m = map(int , input().split())
a = []
for i in range(n) :
    a.append(list(map(int , input().split()))) 
b = []    
if n > m :
    count = 0
    val = n - m
    for i in range(1 , n+1): 
        if(i % 2  == 1):
            if(count < val):
                count += 1 
            else: b.append(a[i-1])
        else :
            b.append(a[i-1])
else:
    count = 0 
    val = m - n 
    for i in range(1 , n + 1):
        c = []
        count = 0
        for j in range(1 , m + 1):
            if(j % 2 == 0):
                if(count < val): count += 1
                else : c.append(a[i-1][j-1])
            else:
                c.append(a[i-1][j-1])
        b.append(c)
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j] , end= " ")
    print()    
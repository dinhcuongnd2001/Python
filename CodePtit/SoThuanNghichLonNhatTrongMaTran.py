def condition(a):
    x = str(a) 
    if(len(x) < 2) : return False
    b = ""
    for i in x:
        b = i + b 
    if(b == x) : return True
    return False

n , m = map(int , input().split())
a = []
for i in range(n): 
    a.append([int(i) for i in input().split()])
ans = -1 
for i in range(n):
    for j in range(m):
        if(condition(a[i][j])):
            ans = max(ans , a[i][j])
if(ans == -1): print("NOT FOUND")
else:
    print(ans)
    for i in range(n):
        for j in range(m):
            if(ans == a[i][j]):
                print("Vi tri [" + str(i) + "][" + str(j) +"]")

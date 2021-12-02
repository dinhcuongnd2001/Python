n = int(input())
a = []
for i in range(n):
    x = [] 
    for j in input():
        x.append(j)
    a.append(x)
count = 0
for i in range(n):
    for j in range(n):
        if(i == 0):
            if(a[i][j] == a[n-1][j] and a[i][j] == "C"):
                count += 1
                print(10,i,j)
        if(j == 0):
            if(a[i][j] == a[i][n-1] and a[i][j] == "C"):
                count += 1
                print(20,i,j)
        if(j < n-1):
            if(a[i][j] == a[i][j+1] and a[i][j] == "C"):
                count += 1
                print(30,i,j)
        if(i < n-1):
            if(a[i][j] == a[i+1][j] and a[i][j] == "C"):
                count += 1
                print(40,i,j)
print(count)
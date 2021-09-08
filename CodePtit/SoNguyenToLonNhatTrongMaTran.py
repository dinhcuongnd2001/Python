import math

def isPrime(n):
    if n < 2 : return False
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0 : return False
    return True

n , m = map(int , input().split())
a = []
for i in range(n): 
    a.append([int(i) for i in input().split()])
ans = -1 
for i in range(n):
    for j in range(m):
        if(isPrime(a[i][j])):
            ans = max(ans , a[i][j])
if(ans == -1): print("NOT FOUND")
else:
    print(ans)
    for i in range(n):
        for j in range(m):
            if(ans == a[i][j]):
                print("Vi tri [" + str(i) + "][" + str(j) +"]")

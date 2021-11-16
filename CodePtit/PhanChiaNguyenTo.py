import math
n = int(input())
a = list(map(int , input().split( )))
b = []

def isPrime(n):
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(len(a)):
    if ((a[i] in b) == False):
        b.append(a[i])
totalSum = sum(b)
check = True
for i in range(len(b)):
    sumIndex = sum(b[0:(i+1)])
    if(isPrime(sumIndex) and isPrime(totalSum - sumIndex)):
        print(i)
        check = False
        break
if(check): print("NOT FOUND")

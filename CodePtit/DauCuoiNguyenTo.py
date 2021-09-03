import math

def isPrime(a):
    if a < 2 : return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if(a % i == 0) : return False
    return True

test = int(input())
for i in range(test):
    a = input()
    b = int(a[0:3])
    c = int(a[len(a)-3 :])
    if(isPrime(b) and isPrime(c)):
        print("YES")
    else :
        print("NO")
import math

def isPrime(a):
    if a < 2: return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if a % i == 0 :
            return False
    return True 

def condition(a):
    for i in range(len(a)):
        if(isPrime(i)):
            if(not isPrime(int(a[i]))) : return False
        else:
            if(isPrime(int(a[i]))) : return False
    return True 

test = int(input())
for i in range(test):
    a = input()
    if(condition(a)): print("YES")
    else: print("NO")
import math
from typing import Literal

def isPrime(a):
    if a < 2 : return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if(a % i == 0) : return False
    return True

def check(a):
    if(not isPrime(len(a))) : return False 
    count = 0 
    for i in range(len(a)):
        if(isPrime(int(a[i]))):
            count += 1
    if(count > (len(a) - count)): return True
    return False

test = int(input())
for i in range(test):
    a = input()
    if(check(a)) : 
        print("YES")
    else : 
        print("NO")
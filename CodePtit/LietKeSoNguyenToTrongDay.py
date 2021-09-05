import math
def isPrime(a):
    if a < 2 : return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if(a % i == 0) :
            return False
    return True
n = int(input())
a = [int(i) for i in input().split()]
store = [0] * 1_000_000
for i in range(n):
    if(isPrime(a[i])):
        store[a[i]] += 1 
for i in range(n):
    if store[a[i]] > 0 :
        print(a[i] , store[a[i]])
        store[a[i]] = 0

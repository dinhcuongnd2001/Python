import math
def isPrime(n):
    if n < 2 : return False
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0 :
            return False
    return True

n = int(input())
a = list(map(int , input().split()))
Prime = []
indexPrime = []
for i in range(len(a)) :
    if isPrime(a[i]):
        Prime.append(a[i])
        indexPrime.append(i)
Prime.sort()
# print(Prime)
# print(indexPrime)
j = 0 
for i in range(len(a)):
    if (i in indexPrime) == False:
        print(a[i], end= " ")
    else :
        print(Prime[j] , end= " ")
        j += 1
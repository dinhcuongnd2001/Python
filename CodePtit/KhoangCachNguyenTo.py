import math
def isPrime(a):
    if a < 2: return False
    for i in range(2, int(math.sqrt(a) +1 )):
        if(a % i == 0) : return False 
    return True 

a , b = map(int , input().split())

ans = b
print(ans , end= ' ')
ans = b + 2 
print(ans , end= ' ')
if(a >= 2): 
    i = 3 
    count = 2
    while count <= a :
        if(isPrime(i)):
            ans += i
            print(ans, end= " ")
            count += 1
        i += 2
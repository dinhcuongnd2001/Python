import math 
def isPrime(n):
    if(n < 2) : return False
    for i in range(2 , (int(math.sqrt(n)) + 1)):
        if n % i == 0 : 
            return False
    return True 

n = int(input())
a = list(map(int , input().split()))
res = 0
for i in a :
    if (not isPrime(i) ) :
        ans = 1001
        val , k = i , 0 
        while(not isPrime(val)):
            val += 1 
            k += 1 
        ans = min(k , ans)
        val , k = i , 0 
        while (not isPrime(val)) and (val >= 2) :
            val -= 1
            k += 1
        ans = min(k , ans) 
        res = max(res , ans)
print(res)
    

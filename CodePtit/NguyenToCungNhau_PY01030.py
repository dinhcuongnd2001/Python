import math 
n , k = map(int , input().split())
count  = 1 
for i in range(10 **(k-1) , 10 **k):
    if(math.gcd(n , i) == 1):
        if(count == 10 ) : 
            print(i , end="\n")
            count = 1
        else :
            print(i , end=" ")
            count += 1 
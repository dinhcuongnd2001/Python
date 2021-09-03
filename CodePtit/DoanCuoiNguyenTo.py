import math 
def isPrime(a):
    if a < 2 : return False
    for i in range(2 , int(math.sqrt(a)) + 1) :
        if(a % i == 0) : return False
    return True 

test = int(input())
for i in range(test):
    a = input()
    b = int(a[len(a)-4 : ])
    # print(b , type(b))
    if(isPrime(b)):
        print("YES")
    else: print("NO")
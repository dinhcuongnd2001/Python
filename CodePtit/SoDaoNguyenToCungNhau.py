import math
test = int(input())
for i in range(test):
    a = input() 
    b = "".join(str(i) for i in list(reversed(a)))
    a = int(a) 
    b = int(b)
    if(math.gcd(a , b) == 1):
        print("YES")
    else : 
        print("NO")

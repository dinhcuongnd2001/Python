import math 
test = int(input())

def UCLN(a , b):
    while (b):
       a , b = b , a % b
    return a

def sum(a):
    res = 0 
    while a > 0 :
        res += (a % 10)
        a //= 10
    return res

def snt(x):
    if x < 2 : return False
    i = 2
    while i <= math.sqrt(x):
        if(x % i == 0): return False
        i += 1
    return True 


while test > 0 :
    a = input().split(" ")
    a = [int(i) for i in a] 
    ans = sum(UCLN(a[0] , a[1]))
    if(snt(ans)):
        print("YES")
    else : print("NO")
    test -= 1


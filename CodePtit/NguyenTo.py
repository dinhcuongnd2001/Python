import math
def snt(a) :
    if(a < 2): return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if(a % i == 0) : return False
    return True

if __name__ == "__main__":
    test = int(input())
    for x in range(test):
        count = 0 
        n = int(input())
        for i in range(1,n+1):
            if(math.gcd(i , n) == 1):
                count += 1
        if(snt(count)): print("YES")
        else : print("NO")

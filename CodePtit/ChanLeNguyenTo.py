import math
def isPrime(a):
    if(a < 2): return False
    for i in range(2 , int(math.sqrt(a)) + 1):
        if(a % i == 0) :
            return False
    return True

def condition1(a):
    for i in range(0 , len(a) , 2):
        if (int(a[i]) % 2 == 1) :
            return False
    return True

def condition2(a):
    for i in range(1 , len(a) , 2):
        if(int(a[i]) % 2 == 0) :
            return False
    return True 

def condition3(a):
    sum = 0 
    for i in range(len(a)):
        sum += int(a[i])
    if(isPrime(sum)):
        return True
    return False

if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        a = input()
        if(condition1(a) and condition2(a) and condition1(a)):
            print("YES")
        else:
            print("NO")

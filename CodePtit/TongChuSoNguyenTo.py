import math
def isPrime(a):
    if(a < 2): return False 
    for i in range(2 , int(math.sqrt(a)) + 1) :
        if(a % i == 0): return False
    return True 

def solve(a):
    sum = 0
    for i in range(len(a)):
        sum += int(a[i])
    if(isPrime(sum)): print("YES")
    else: print("NO")

if __name__ == '__main__':
    test = int(input()) 
    for i in range(test):
        a = input();        
        solve(a)
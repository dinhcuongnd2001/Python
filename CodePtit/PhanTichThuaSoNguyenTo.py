import math

def pt(a):
    ans = "1 * "
    count = 0 
    while a % 2 == 0:
        count += 1 
        a //= 2
    if count > 0 and a > 1 :
        ans = ans + "2^" + str(count) + " * "
    elif count > 0 and a == 1:
        ans = ans + "2^" + str(count)
    for i in range(3, int(math.sqrt(a)) + 1 , 2):
        count = 0
        while a % i == 0:
            count += 1 
            a //= i 
        if(count > 0 and a == 1):
            ans = ans  + str(i) +"^" + str(count)
        elif count > 0 :
            ans = ans  + str(i) +"^" + str(count) + " * "
    if a > 1 : ans = ans + str(int(a)) + "^1" 
    print(ans)

if __name__ == "__main__":

    test = int(input())
    for i in range(test):
        a = int(input())
        pt(a) 


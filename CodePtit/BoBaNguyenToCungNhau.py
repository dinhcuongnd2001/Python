import math
L , R = map(int , input().split())
a = [] 
store = []

for i in range(L , R + 1):
    for j in range(i +1 , R + 1):
        if(math.gcd(i , j) != 1):
            continue
        for k in range(j+1 , R+1):
            a = []
            if(math.gcd(j , k) != 1):
                continue
            if(math.gcd(i , j) == 1 and math.gcd(i , k) == 1 and math.gcd(j , k) == 1):
                a.extend([i , j , k])
                # print(a)
                store.append(a)
if(len(store) == 0): print("NO")
else :
    for i in range(len(store)):
        print('({} , {} , {})'.format(store[i][0] , store[i][1] , store[i][2]))
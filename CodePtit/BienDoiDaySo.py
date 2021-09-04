
from abc import abstractmethod


while(True):
    a = input().split()
    if(a[0] == '0' and a[1] == '0' and a[2] == '0' and a[3] == '0'):
        break 
    else:
        a = [int(i) for i in a] 
        count = 0 
        a.insert(0 , 0)
        while(not(a[1] == a[2] and a[1] == a[3] and a[1] == a[4])):
            a[0] = a[1]
            for i in range(1, 4):
                a[i] = abs(a[i] - a[i+1])
            a[4] = abs(a[4] - a[0])
            count += 1
        print(count)    

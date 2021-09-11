test = int(input())
for i in range(test):
    n , m , k = map(int , input().split())
    a = list(map(int , input().split()))
    b = list(map(int , input().split()))
    c = list(map(int , input().split()))
    maxHead = max(a[0] , max(b[0] , c[0]))
    minTail = min(a[-1] , min(b[-1] , c[-1]))
    i , j , k = 0 , 0 , 0 
    check = True 
    while(maxHead <= minTail):
        if(maxHead == a[i] and maxHead == b[j] and maxHead == c[k]):
            print(maxHead , end= " ")
            check = False 
            i += 1
            j += 1
            k += 1
        else:
            while(a[i] < maxHead): i += 1 
            while(b[j] < maxHead): j += 1
            while(c[k] < maxHead): k += 1
        if(i >= len(a) or j >= len(b) or k >= len(c)):
            break
        maxHead = max(a[i] , max(b[j] , c[k])) 
    if(check): print("NO")
    print()
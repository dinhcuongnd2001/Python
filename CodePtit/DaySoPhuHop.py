#idea: sap xep 2 day so roi cho 1 vong for kiem tra dk : 
#neu a[i] > b[i] : print("NO")
#neu chay het: print("YES")
test = int(input())
for i in range(test):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort() 
    check = True
    for i in range(n) :
        if(a[i] > b[i]):
            print("NO") 
            check = False   
            break
    if(check): print("YES")
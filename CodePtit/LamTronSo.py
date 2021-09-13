test = int(input())
for j in range(test):
    a = input()
    if(int(a) <= 10):
        print(a)
        continue
    c = 0
    tail = int(a[len(a) - 1]) 
    if(tail >= 5): c += 1
    for i in range(len(a) - 2 , -1 , -1):
        if a[i] <= str(9 - c):
            tail = int(a[i]) + c
            c = 0  
        else:
            tail = 0 
            c += 1
        if tail >= 5:
            c += 1
    if tail == 0 :
        ans = "1" 
        ans = ans + '0' * len(a)
    else:
        ans = str(tail)
        ans = ans + '0' * (len(a) - 1)
    print(ans)

while(True):
    n = int(input())
    if(n == 0) : break
    else:
        a = []
        for i in range(n):
            a.append(int(input()))
        a.sort()
        if(a[0] == a[len(a) - 1]): print("BANG NHAU")
        else: print(a[0] , a[len(a) - 1])

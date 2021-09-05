test = int(input())
for i in range(test):
    store = [0] * 1001
    a = []
    n = int(input())
    for i in range(n): 
        x = int(input())
        a.append(x) 
        store[x] += 1
    a.sort()
    ans = 0 
    res = 0
    for i in range(len(a) -1 , -1 , -1):
        if ans <= store[a[i]]:
            ans = store[a[i]]
            res = a[i]
    print(res)
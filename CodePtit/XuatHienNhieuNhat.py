test = int(input())

for t in range(test):
    n = int(input())
    a = input().split()
    a = [int(i) for i in a]
    mark = [0] * 1000005
    for i in a:
        mark[i] += 1
    x , y = 0 , 0
    for i in a:
        if mark[i] > x : 
            x = mark[i]
            y = i 
    if x > n/2 :
        print(y)
    else:
        print("NO")
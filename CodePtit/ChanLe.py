t = int(input())

while t > 0:
    a = list(input())
    a = [int(i) for i in a]
    sum = a[0]
    test = True
    i = 1 
    while i < len(a):
        if(abs(a[i] - a[i-1]) != 2):
            print("NO")
            test = False 
            break
        else: sum += a[i]
        i += 1
    if(test):
        if(sum % 10 == 0) : print("YES") 
        else: print("NO")
    t -= 1 

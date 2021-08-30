test = int(input())

while test > 0 :
    strA = input()
    a = list(strA)
    i = 1
    check = True
    while i < len(a):
        if(a[i] < a[i-1]):
            print("NO") 
            check = False
            break
        i += 1
    if(check): print("YES")
    test -= 1   
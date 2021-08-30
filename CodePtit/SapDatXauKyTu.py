test = int(input())
count = test
while test > 0:
    test -= 1 
    check = True
    strA = input()
    strB = input()
    if(len(strA) != len(strB)):
        check = False
    else:
        a = sorted(strA)
        b = sorted(strB)
        i = 0 
        while i < len(a):
            if(a[i] != b[i]):
                check = False
                break
            i += 1
    if(check): print("Test " + str(count - test) + ": YES")     
    else : print("Test " + str(count - test) + ": NO")
    
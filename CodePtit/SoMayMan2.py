t = int(input())
while t > 0:
    strA = input()
    test = True 
    for i in strA:
        if(int(i) != 4 and int(i) != 7):
            test = False 
            print("NO")
            break
    if(test): print("YES")
    t -= 1
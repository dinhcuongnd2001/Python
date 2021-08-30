strA = input()
strB = input()
p = int(input())
if(p == 1):
    print(strB + strA)
elif(p == len(strA)): 
    print(strA + strB)
else:
    print(strA[0:p-1] + strB + strA[p-1:len(strA)])

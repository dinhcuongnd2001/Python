def tong(a):
    sum = 0 
    for i in range(1 , len(a) , 2):
        sum += int(a[i])
    print(sum)
def tich(a):
    mul = 1 
    check = False
    for i in range(0 , len(a) , 2):
        if(int(a[i]) != 0):
            mul *= int(a[i])
            check = True
    if(not check) : print(0)
    else: print(mul , end= " ")

test = int(input())
for i in range(test):
    a = input()
    tich(a)
    tong(a)
    
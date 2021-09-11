def condition(a):  
    x1 = str(a)
    x2 = ''
    for i in range(len(x1) - 1 , -1 , -1):
        x2 += x1[i]
        if(int(x1[i]) % 2 == 1): return False
    if(x2 == x1 and len(x1) % 2 == 0):
        return True
    return False

if __name__== "__main__":
    test = int(input())
    for i in range(test):
        a = int(input())
        val = 22
        for x in range(22, 89 ,2):
            if(val > a):
                break
            if(condition(x)):
                print(x, end= " ")
            val = x
        val = 2222
        for x in range(2222, 8889,2):
            if(val > a):
                break
            if(condition(x)):
                print(x, end= " ")
            val = x 
        val = 222222
        for x in range(222222 , 888889 ,2):
            if(val > a):
                break
            if(condition(x)):
                print(x, end=" ")
            val = x
        val = 22222222
        for x in range(22222222 , 88888888 , 2):
            if(val > a):
                break
            if(condition(x)):
                print(x, end=" ")
            val = x
        print(end="\n")
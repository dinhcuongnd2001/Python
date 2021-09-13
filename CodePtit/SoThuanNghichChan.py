#sinh xau nhi phan doi xung
a = [0, 2, 4, 6, 8]
def condition(a):  
    x1 = str(a)
    x2 = ''
    for i in range(len(x1) - 1 , -1 , -1):
        x2 += x1[i]
        if(int(x1[i]) % 2 == 1): return False
    if(x2 == x1 and len(x1) % 2 == 0):
        return True
    return False

# def Try(i):


if __name__== "__main__":
    test = int(input())
    for i in range(test):
        a = int(input())
        
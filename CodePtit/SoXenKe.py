def condition1(a):
    if(len(a) % 2 == 1):
        return True
    return False 
def condition2(a):
    if(a[0] == a[1]):
        return False
    return True
def condition3(a):
    for i in range(len(a) - 2):
        if(int(a[i]) != int(a[i+2])):
            return False
        return True 

if __name__ == "__main__":
    test = int(input()) 
    for i in range(test):
        a = input()
        if(condition1(a) and condition2(a) and condition3(a)):
            print("YES")
        else : print("NO")

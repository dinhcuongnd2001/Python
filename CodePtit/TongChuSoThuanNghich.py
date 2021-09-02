def check(a):
    if(len(a) == 1): return False
    else:
        i = 0 
        while(i <= len(a)/2):
            if a[i] != a[len(a) - i -1]: return False
            i += 1 
    return True
    
if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        a = input()
        sum = 0 
        for i in range(len(a)):
            sum += int(a[i])
        if(check(str(sum))): print("YES")
        else : print("NO")
    
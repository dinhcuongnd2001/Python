if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        a = input()
        sum = 0 
        for i in range(len(a)) :
            sum += int(a[i])
        if(sum % 3 == 0): print("YES")
        else : print("NO")
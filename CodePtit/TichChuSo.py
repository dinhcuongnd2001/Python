if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        a = input()
        ans = 1
        for i in range(len(a)):
            if(int(a[i]) != 0):
                ans *= int(a[i])
        print(ans)
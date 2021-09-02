if __name__ == "__main__" :
    a, k, n = map(int, input().split())
    check = False
    for i in range(k, n + 1, k):
        if i <= n and i - a >= 1:
            print(i - a, end = " ")
            check = True
    if not check:
        print(-1)
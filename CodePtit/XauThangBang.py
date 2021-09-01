test = int(input())

for i in range(test):
    a = input()
    #dao nguoc a thanh c:
    c = ''.join(str(i) for i in list(reversed(a)))
    test = True
    for i in range(len(a) - 1):
        if(abs(ord(a[i]) - ord(a[i+1])) != abs(ord(c[i]) - ord(c[i+1]))):
            print("NO")
            test = False
            break
    if(test): print("YES")
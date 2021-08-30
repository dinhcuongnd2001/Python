test = int(input())

while(test > 0) : 
    strA = input()
    a = list(strA)
    ans = ""
    i = 0
    str1 = ""
    while i < len(a):
        if(i % 2 == 1):
            ans = ans + str1 * int(a[i])
            str1 = ""
        else:
            str1 += a[i]
        i += 1
    print(ans)
    test -= 1


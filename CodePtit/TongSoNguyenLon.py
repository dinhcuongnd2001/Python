a = input()
b = input()
if(a == '0'*len(a) and b == '0' * len(b)):
    print(0)
else:
    if(len(a) < len(b)) : a , b = b , a
    #chuan hoa 2 xau cho co do dai bang nhau
    b = '0' * (len(a) - len(b)) + b
    #print(a , b)
    # bien c la de luu trang thai phep tinh (= 1 la nho)
    c = 0 
    ans = ''
    for i in range(len(a) - 1 , -1 , -1):
        tg = int(a[i]) + int(b[i]) + c
        if(tg > 9):
            tg -= 10 
            c = 1
        else : c = 0
        ans = str(tg) + ans
    if c == 1: ans = str(c) + ans
    k = 0
    while(ans[k] == '0'): k += 1
    ans = ans[k:]
    print(ans)
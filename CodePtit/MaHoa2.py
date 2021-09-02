p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while(True):
    srtA = input()
    k = 0 
    s = ""
    for i in srtA:
        if i >= '0' and i <= '9':
            k = k*10 + int(i)
        else:
            if(i != ' '):
                s += i
    if(k == 0) : break
    else:
        a = list(s)
        ans = ""
        for i in range(len(a)):
            index = p.find(a[i])
            ans = p[(index + k) % 28] + ans 
        print(ans)
   
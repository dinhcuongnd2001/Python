a = input()
ans = set()
for i in range(0 , len(a) - 1 , 2):
    tg = int(a[i: i+2]) 
    if (tg in ans) == False :
        ans.add(tg)
        print(tg , end= " ")


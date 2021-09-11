n , m = map(int , input().split())
dic = {}
a = list(map(int , input().split()))
for i in a:
    dic[i] = (1 + dic.setdefault(i , 0))

ans = sorted(set(list(dic.values())))
if(len(ans) == 1):
    print("NONE")
else : 
    x = sorted(dic) 
    for i in x :
        if(dic[i] == ans[-2]):
            print(i)
            break
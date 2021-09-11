a = input()
k = int(input())
dic = {} 
for i in range(0 , len(a) - 1, 2):
    val = int(a[i : i + 2])
    dic[val] = 1 + dic.setdefault(val , 0)
check = True
ans = sorted(dic)
for i in ans:
    if(dic[i] >= k):
        check = False
        print(i , dic[i])
if(check):
    print("NOT FOUND")

import re
n, k = map(int, input().split(" "))

a={}
for i in range(n):
    s = re.sub('[^a-zA-Z]',' ',input()).strip().lower()
    pattern = "\s+"
    x =re.split(pattern,s)
    for x1 in x:
        a[x1] = a.setdefault(x1,0) + 1
ans = sorted(a.items(), key=lambda x : x[0])
ans = sorted(ans,reverse=True,key=lambda x : x[1])
for i in ans:
    if i[1] >= k:
        print("{} {}".format(i[0], i[1]))

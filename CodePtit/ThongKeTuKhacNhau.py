import re
n = int(input())
store = {}
for i in range(n):
    s = re.sub('[^a-zA-Z0-9 \n]',' ', input()).strip().lower()
#    print(s)
    pattern = "\s+"
    a = re.split(pattern, s)
    for x in a:
        store[x] = store.setdefault(x, 0) + 1
ans = sorted(store.items(), key = lambda x : x[0])
# print(type(ans))
ans = sorted(ans, reverse=True,key=lambda x: x[1])
for i in ans:
    print("{} {}".format(i[0], i[1]))

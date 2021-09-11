n  , m = map(int , input().split())
a = []
minA = 10000 
maxA = -1

for i in range(n):
    b = [int(i) for i in input().split()]
    minA = min(minA , min(b))
    maxA = max(maxA , max(b))
    a.append(b)
# print(minA , maxA)
luckyValue = maxA - minA
ans = [] 
for i in range(n):
    for j in range(m):
        mark = []
        if(a[i][j] == luckyValue):
            mark = [i , j]
            ans.append(mark)
if(len(ans) > 0):
    print(luckyValue)
    for i in range(len(ans)):
        print("Vi tri [{}][{}]".format(ans[i][0] , ans[i][1]))
else:
    print("NOT FOUND")

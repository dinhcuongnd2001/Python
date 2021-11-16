n = int(input())
a = []
ans = []
totalSum = 0 
for i in range(n):
    b =  [ int(i) for i in input().split(' ')]
    a.append(b)
    totalSum += sum(b)
totalSum //= (n-1) * 2

if n == 2:
    print(1 , a[0][1] -1)
else:
    for i in range(n):
        mark = sum(a[i])
        res = (mark - totalSum)//(n-2)
        ans.append(res)
    for i in range(len(ans)):
        print(ans[i] , end= " ")
    print()
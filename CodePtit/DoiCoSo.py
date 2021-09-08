a = []
for i in range(10):
    a.append(i)
for i in range(65,91):
    a.append(chr(i))

def solve(N , b):
    ans = "";
    while(N > 0):
        tg = N % b
        ans = str(a[tg]) + ans
        N //= b 
    print(ans)
test = int(input())
for i in range(test):
    N , b = map(int , input().split())
    solve(N , b)

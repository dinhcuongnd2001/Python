import math
def countNum(n):
    s = str(n)
    return len(s)
def solve(n):
    s = str(n)
    ans = 0
    for x in s:
        if x == '-':
            ans += ord('-') - ord('0')
            continue
        ans += int(x)
    return ans

n = int(input())
count = 0
while(countNum(n) > 1):
    n = solve(n)
    count += 1
print(count)
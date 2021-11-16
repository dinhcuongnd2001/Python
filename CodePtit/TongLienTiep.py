import math

def handle(n):
    return n * (n + 1) / 2

test = int(input())
for i in range(test):
    num = int(input())
    cnt = 0
    id = 1
    r = 50000
    l = 2
    limit = r
    while l <= r:
        m = (int)(l + r) /2
        if handle(m) > num:
            r = m - 1
            limit = m
        else : l = m + 1
    for i in range(1, (int)(limit) , id):
        if i == 1: continue
        if i % 2 == 1:
            if num % i == 0 and num - handle(i - 1) > 0:
                cnt += 1
        elif i % 2 == 0:
            if num % i == i / 2 and num - handle(i - 1) > 0:
                cnt += 1
    print(cnt)
n = int(input())
a = input().split() 
a = [int(i) for i in a] 
count = 0
for i in range(n -1):
    for j in range(i + 1, n):
        if(a[i] > a[j]):
            count += 1
print(count)
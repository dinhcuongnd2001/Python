n = int(input())
matrix = []
for i in range(n):
    a = [int(i) for i in input().split()]
    matrix.append(a) 

k = int(input())
sum1 = 0
sum2 = 0 
for i in range(n):
    for j in range(n):
        if(i < j):
            sum1 += matrix[i][j]
        if(i > j):
            sum2 += matrix[i][j]
if(abs(sum1 - sum2) <= k):
    print("YES")
else : print("NO")
print(abs(sum1 - sum2))

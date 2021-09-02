import math
#nhap
a = input().split()
n = int(a[0]) 
m = int(a[1])

matrix = [] 
for i in range(n):
    matrix.append(input().split())
# ham kiem tra ngto
def checkIsPrime(a):
    if a < 2: 
        return False
    for i in range(2 , int(math.sqrt(a) + 1) , 1) :
        if a % i == 0:
            return False
    return True
# mang de luu String cho viec in    
ans = []
# kiem tra tung phan tu co la so ngto k
for i in range(n):
    strA = ""
    for j in range (m):
        if(checkIsPrime(int(matrix[i][j]))):
            matrix[i][j] = 1 
        else :
            matrix[i][j] = 0 
        strA = strA + str(matrix[i][j]) + " "
    ans.append(strA)

for i in range(n):
    print(ans[i])


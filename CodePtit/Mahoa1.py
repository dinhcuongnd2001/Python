test = int(input())
def solve(a):
    a += "."
    strA = ""
    count = 1
    for i in range(len(a) - 1):
        if(a[i] == a[i+1]):
            count += 1 
        else:
            strA = strA + str(count) + a[i]
            count = 1 
    
    print(strA)

for i in range(test):
    strA = input()
    solve(strA)
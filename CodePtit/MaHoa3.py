test = int(input())
store = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def Rotate(x):
    val = 0
    res = ''
    for s in x :
        val += (ord(s) - ord('A'))
    for s in x:
        res += store[(ord(s) - ord('A') + val) % 26]
    return res

def Merge(x):
    mid = len(x)//2 
    x1 = Rotate(x[0 : mid])
    x2 = Rotate(x[mid: len(x)+ 1])
    ans = ''
    for i in range(len(x1)):
        index = ((ord(x1[i]) - ord('A')) + (ord(x2[i]) - ord('A'))) % 26
        ans += store[index]
    print(ans)

for i in range(test):
    x = input()
    Merge(x)


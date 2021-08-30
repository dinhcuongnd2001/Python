test = int(input())

while test > 0:
    a = input()
    mark = list(a)
    mark = [int(i) for i in mark]
    length = len(mark)
    if(mark[0] == mark[length-2] and mark[1] == mark[length-1]):
        print("YES")
    else: 
        print("NO")
    test -= 1 
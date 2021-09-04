n = int(input())
a = input().split()
a = [int(i) for i in sorted(a)]
for i in range(1 , 30001):
    if (i in a) == False:
        print(i)
        break
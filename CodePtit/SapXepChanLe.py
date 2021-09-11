n = int(input())
a = []
while len(a) < n :
    a.extend(list(map(int , input().split())))
even = []
indexEven = []
odd = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        even.append(a[i]) 
        indexEven.append(i)
    else:
        odd.append(a[i])
even.sort()
odd.sort(reverse = True)
# print(even)
# print(odd)
x , y = 0 , 0
for i in range(len(a)):
    if (i in indexEven) == True:
        print(even[x] , end= " ")
        x += 1
    else:
        print(odd[y] , end= " ")
        y += 1
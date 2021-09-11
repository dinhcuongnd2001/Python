a = input()
b = []
for i in range(0 , len(a) - 1  , 2):
    val = int(a[i : i +2]) 
    b.append(val) 
ans = sorted(set(b))
for i in ans:
    print(i , end= " ")
print()
n = int(input())
a = list(map(int , input().split())) 
store = {}
for i in a:
    store[i] = 1 + store.setdefault(i , 0) 
for i in range(len(a)):
    sum = 0 
    for j in range(len(a)):
        sum += abs(a[i] - a[j]) 
    store[a[i]] = sum 
ans = min(list(store.values()))
print(ans , end=" ")
for i in a :
    if(ans == store[i]):
        print(i)
        break
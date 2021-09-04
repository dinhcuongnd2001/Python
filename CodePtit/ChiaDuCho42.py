t = 0
a = []
while(t < 10 ):
    x = int(input())
    a.append(x)
    t += 1
    
store = [-1]
for i in a :
    if (i % 42 in store) == False:
        store.append(i % 42)
    
print(len(store) - 1)
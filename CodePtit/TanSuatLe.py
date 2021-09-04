test = int(input())

for i in range(test):
    n = int(input())
    store = [0] * 1_000_000
    a = input().split()
    for i in a :
        store[int(i)] += 1
    for i in a :
        if(store[int(i)] % 2 == 1):
            print(i)
            break

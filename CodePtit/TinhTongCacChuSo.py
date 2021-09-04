test = int(input())

for i in range(test):
    a = input() 
    sum = 0 
    b = ""
    for i in range(len(a)):
        if(a[i] >= '0' and a[i] <= '9'):
            sum += int(a[i])
        else:
            b += a[i] 
    b = "".join(sorted(b))
    print(b + str(sum))

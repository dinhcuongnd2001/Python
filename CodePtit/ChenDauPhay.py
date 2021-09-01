a = list(str(i) for i in reversed(input()))
b = ""
for i in range(len(a)):
    b += a[i]
    if(i % 3 == 2 and i != len(a) -1):
        b += ','
#dao nguoc lai xau b:
b = ''.join(list(str(i) for i in reversed(b)))
print(b)
def convert(a) :
    sum = 0 
    for i in range(3):
        sum += ( int(a[i]) * (2 **(2-i)) )
    return sum 

a = input()
#them so luong so 0 vao cuoi chuoi
length = len(a)
if(length % 3 != 0) : a =  ("0" * (3 - length % 3)) + a
length = len(a)
#print(a)
index = 0
ans = ""
for i in range(2 , length , 3):
    sub = a[index : i+1] 
    index = i + 1
    ans += str(convert(sub))
print(ans)
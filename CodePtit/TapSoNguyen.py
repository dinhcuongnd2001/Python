n , m = map(int , input().split())
a = input().split()
A = sorted(set(a))
b = input().split()
B = sorted(set(b))
for i in A :
    if(i in B): print(i , end= " ")
print(end= "\n")
for i in A :
    if((i in b) == False):
        print(i , end=" ")
print()
for i in B :
    if((i in A) == False):
        print(i , end=" ")
print()


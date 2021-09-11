n , m = map(int , input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
A = sorted(set(a))
B = sorted(set(b))
if(len(A) != len(B)):
    print("NO")
else:
    check = True
    for i in range(len(A)):
        if(A[i] != B[i]):
            check = False 
            print("NO")
            break
    if(check):
        print("YES")
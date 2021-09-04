f = [0] * 100 

def fibonaci():
    f[1] , f[2] = 1 , 1
    for i in range(2 , 93):
        f[i] = f[i-1] + f[i-2]


if __name__ == "__main__":
    test = int(input()) 
    fibonaci()
    for i in range(test):
        a , b = map(int , input().split()) 
        for i in range(a , b + 1):
            print(f[i] , end=" ")
        print("\n")
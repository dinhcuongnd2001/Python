

if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        n , x , m = map(float , input().split())
        # print(n , type(n))
        # print(x , type(x))
        # print(m , type(m))
        ans = 1
        val = n*(1 + x/100) 
        while val < m :
            val *= (1 +x/100)
            ans  += 1
        print(ans)

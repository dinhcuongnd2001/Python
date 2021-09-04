import math
n = int(input())
a = input().split() 
a = [float(i) for i in a]
MIN = min(a)
MAX = max(a)
sum = 0 
count = 0
for i in a :
    if(i != MIN and i != MAX):
        sum += i 
        count += 1
print("%0.2f" %(sum /count))
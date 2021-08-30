strA = input()
count = 0 
for i in strA:
    if(int(i) == 4 or int(i) == 7) : count += 1
if (count == 4 or count == 7):
    print("YES")
else:
    print("NO")
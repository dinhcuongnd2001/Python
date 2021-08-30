strA = input() 
count = 0 
for i in strA:
    if(i.isupper()) : count += 1 
if (count > (len(strA) - count)): print(strA.upper())
else : print(strA.lower())
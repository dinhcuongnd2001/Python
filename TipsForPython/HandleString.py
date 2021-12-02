# Tip 1 :reverse String
'''
a = "hello"
b = a[::-1]
print(b)
'''

#Tip 2: xoa các ký tự đặc biệt trong 1 xâu:
'''
import re
import string
my_str = "hey th~!ere"
my_new_str = re.sub('[^a-zA-Z0-9 \n\.]', '',my_str)
print(my_new_str)
# cach2 :
my_str = "hey th~!ere"
chars = re.escape(string.punctuation)
print (re.sub(r'['+chars+']', '',my_str))
'''

#Tip 3: cat chuoi:

a = "PTIT    duy   tri   hoc    phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!"
# cat chuoi thong thuong theo 1 ky tu chi dinh:
b = a.split(" ")
print(b)
#cat chuoi nang cao:
import re
pattern = "\s+"
print(re.split(pattern, a))

s = "HELLO"
print(s.title())


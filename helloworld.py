
# def triMulti(a,b,c):
#     ''' Nhap vao 3 so nguyen
#         Tra ve tich cua 3 so vua nhap
#     '''
#     return a * b * c 
# a = int(input("a =  "))
# b = int(input("b =  "))
# c = int(input("c =  "))
# print(triMulti(a,b,c))


#
# def main():
#     print ("Hello, Im DNC")

# if __name__ == "__main__" :
#     main() 
# print("Hello, nice to miss you")
# print("Yes me too")

# import math
# def isPrime(n):
#     if n < 2 : return False
#     for i in range(2,int(math.sqrt(n))+ 1):
#         if n % i == 0: return False
#     return True

# def primeList(a):
#     b = []
#     for x in a:
#         if isPrime(int(x)):
#             b.append(x)
#     return b

# a = input("a = ").split(",")

# print(primeList(a))

# def mySort(a):
#     b = []
#     for x in a:
#         b.append(int(x))
#     return sorted(b)
# a = input("a = ").split(',')
# print(mySort(a))

# def isPalindrome(a):
# # reverse String 
#     b = a[::-1]
#     if a == b: return True
#     return False
# a =  input('a = ')
# if(isPalindrome(a)): print('a is a Palindrome')
# else: print('a is not a Palindrome')

def pow(x , y):
    if x < 0 or y < 0 :
        return 
    
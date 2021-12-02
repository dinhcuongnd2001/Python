class Rectangle:
    def __init__(self, a , b , s):
        self.a = a 
        self.b = b
        self.s = s
    def perimeter(self):
        return (self.a + self.b) * 2
    def area(self):
        return self.a*self.b
    def color(self):
        return self.s.title()


if __name__ == '__main__':
    arr = input().split()
    if(int(arr[0]) < 0 or int(arr[1]) < 0):
        print("INVALID")
    else:
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
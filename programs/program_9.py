'''class Speed():
    def __init__(self):
        self.speed = 10
        self.__new_speed = 20
    def get_new_speed(self):
        return (self.__new_speed)
    def set_new_speed(self,__new_speed):
        self.__new_speed = __new_speed
s = Speed()
s.set_new_speed(200)
print(s.get_new_speed())'''


'''class Books:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return self.pages + other.pages
    def __mul__(self,other):
        return self.pages * other.pages
b1 = Books(100)
b2 = Books(150)

print(b1 + b2)
print(b1 * b2)
'''


'''class Python:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return self.pages + other.pages
    def __gt__(self,other):
        return self.pages > other.pages

    def __sub__(self,other):
        return self.pages - other.pages

class Java:
    def __init__(self,pages):
        self.pages = pages
b1 = Python(200)
b2 = Java(100)

print(b1 + b2)
print(b1 > b2)
print(b1 - b2)
'''

x = int(input('enter your number'))
y = int(input('enter your number'))



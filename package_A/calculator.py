def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mulp(x,y):
    return x * y
def devide(x,y):
    return x / y


operator = input("select operator +-*/  ")
num1 = int(input("enter your frist number "))
num2 = int(input("enter your second number  " ))
if operator == '+':
    print(num1, "+", num2,"=", add(num1,num2))

elif operator == '-':
    print(num1, "-", num2,"=", sub(num1,num2))

elif operator == '*':
    print(num1, "*", num2,"*", mulp(num1,num2))

else:
    print(num1, "/", num2,"=", devide(num1,num2))
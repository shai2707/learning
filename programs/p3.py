
def area_of_triangle(a,b,c):
    s= (a+b+c)/2
    A= (s*(s-a) *(s-b)* (s-c))**0.5
    return A
x=area_of_triangle(1,2,3)
print(x)
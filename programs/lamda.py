lambda x: x+y
sum = lambda x,y: x+y
print(sum(1,2))



#def show(a):
#show(5)


'''show = lambda a : print(a)
show(5)



add = lambda x,y : x+y
print(add(2,3))'''

add_sub = lambda x, y = (x + y, x - y)
a , s = add_sub(4,2)
print(a)

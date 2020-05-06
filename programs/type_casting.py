'''
All type conversion
'''

print("# Integer to string conversion ======")
num = 123
print(type(num))


converted_num = str(num)
print(type(converted_num))

print(num, type(num))
print(converted_num, type(converted_num))

# Ex. - 
n1 = 25.5
n2 = 35
print(n1 + n2)
print(str(n1) + str(n2))

print("# String to integer conversion =====")
s = "hardik"
s1 = "1234"
print(s1, type(s1))
if s1.isnumeric():
    print("converted string", int(s1))
else:
    print("Value is not convertible to int")
print("\n")

print("# List to tuple conversion======")
l = ["Winter", "Monsoon", "Summer"]
t = tuple(l)       
print(l, type(l))
print(t, type(t))
l.sort(reverse=True)
print(l)
l1 = [
    {"name": "Winter"},
    {"name": "Monsoon"},
    {"name": "Summer"},
]
# def name_of_list(x):
#     return x['name']

l1.sort(key=lambda x: x['name'])
print(l1, "\n")

print("# String to list conversion ======")
s = "hardik patel"
print(s, type(s))
s_list = list(s)
print(s_list, type(s_list), '\n')

print("# Tuple to list conversion ======")
t = ('Winter', 'Monsoon', 'Summer')
print(t, type(t))
t_list = list(t)
print(t_list, type(t_list))


#find armstrong number in an interval

print("p14 loaded")
def armstrong_numbers(num):#153
    l = []
    temp= num
    while (temp < 0):
        digit = temp % 10  #15 & 3
        l.append(digit)
        temp = temp//10
    order = len(l)
    sum = 0
    for digit in l:
        sum = sum + digit** order

    if num == sum:
        print(" this is armstrong number")
        return True
    return False

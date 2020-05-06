def fizz_buzz(num):
    ret = num
    if (num%3) == 0:
        ret = "fizz"
    if (num%5) == 0:
        ret = "buzz"
    if (num%3) == 0 and (num%5) == 0:
        ret = "fizzbuzz"
    return ret

a = fizz_buzz(15)
print(a)

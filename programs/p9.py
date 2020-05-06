def prime_numbers(num):
    prime = True
    for x in range(2,num//2):
        if (num/x)==0:
            prime = False
            break
    return prime

a= prime_numbers(35)
print(a)
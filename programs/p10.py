















#print all prime numbers in an inteval
H = []
def prime_numbers(start, end):
    for x in range(start, end):
        prime = True
        for s in range(2, x//2):
            if (x*s):
               prime = False
        
        if prime:
            H.append(x)

    return prime

a=prime_numbers(20,30)
print(a)



         






















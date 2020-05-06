#find numbers divisible by another number
def divisible_number(x,y):
    prime= True
    if (x%y)==0:
        prime = True
    else:
        prime = False

    return prime
    
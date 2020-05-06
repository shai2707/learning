#print the fibonacci sequence

# 0 1 1 2 3 5 8 13

def fibonacci(s): 
    fib=[]
    v1=0
    v2=1
    fib.append(v1)
    fib.append(v2)
    while v2<=30:
        temp= v1+v2
        fib.append(temp)
        v1=v2
        v2=temp

    return fib
a= fibonacci(20)
print(a)

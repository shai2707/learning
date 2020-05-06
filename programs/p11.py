#find the factorial of a numbers
def factorial_numbers(num):
    factorial = 1
    if num<0:
        print("factorial numbers is not nagtive numbers")
    elif num==0:
        print("factorial numbers zero is 1")
    else:
        for x in range(1,num+1):
            factorial = factorial*x
        print(factorial)

factorial_numbers(5)


        

            
                
             
            



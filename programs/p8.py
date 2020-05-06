#check if a year is leap or not
def check_leap_year(year):
    prime = True 
    if(year % 4)==0:
        if(year % 100)!=0:
            pime = False
        else:
            if(year % 400)==0:
                prime = True
    else:
        prime = False
    return prime
a=check_leap_year(2000)
print(a)
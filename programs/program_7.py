def sum_numbers(num):
    sum = 0
    privious = 0
    for num in range(10):
        sum = privious + num 
        print("current num: ", num, "privious number: ", privious , "sum: ", sum)
print("printing current and privious numbers sum in given  range(10)")    
sum_numbers(10)  
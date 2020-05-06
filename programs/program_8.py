def even_index_number(str):
    for i in range(0, len(str)-1,2):
        print('index[i]', str[i] )

inputstr = input("please enter your string  ")
print("original string: " , inputstr)

print("printing only even index chers")
even_index_number(inputstr)


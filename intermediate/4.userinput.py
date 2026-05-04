
# ##note that by default input is a string
# a=input('enter your name: ')
# print(a) # if input is ram and output is ram
# print(a[0]) # if input is ram then the output is r, as we told input is string

# so the best way to do that only the first corect print if we need, then
# a=input('enter your name:')[0] #now the memory is also saved as only first character is stored
# print(a) #this will only print the first character of the string





##
# a = input("Enter first value: ")
# b = input("Enter second value: ")
# c=a+b  #note that this will not work as input is string


## so to make them work we need to convert the input into the integer


a= int(input('Enter the first num: '))
b= int(input('Enter the second num: '))
c= a+b
print(c)









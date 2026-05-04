

a = 5
b = 7
print(a, b, sep=', ')  # 5, 7

# Swap the variables
c = a
a = b
b = c
print('a:', a, 'b:', b, sep=', ')  # a:, 7, b:, 5


## swap the variables without third variable using subtraction and addition

a= 3
b= 8
a= a+b
b=a-b
a=a-b
print('a:', a, 'b:', b, sep=', ') #a:, 8, b:, 3


##swap the variable multiplication and division
a= 3
b= 8
a= a*b
b=a//b ##note that // gives the float value
a=a//b ##note that // gives the float value
print('a:', a, 'b:', b, sep=', ') #a:, 8, b:, 3




##XOR using, but generally not used

a = 3
b = 8
a = a ^ b  # a = 11 (1011 in binary)
b = a ^ b  # b = 3
a = a ^ b  # a = 8
print('a:', a, 'b:', b, sep=', ') #a:, 8, b:, 3



##but here is the one of the best way using tuple in python

a = 3
b = 8
a, b = b, a  #here not overwriting the values as it is doing tupple packing and tupple unpacking
print('a:', a, 'b:', b, sep=', ') #a:, 8, b:, 3




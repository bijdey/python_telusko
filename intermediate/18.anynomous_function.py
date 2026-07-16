#459
#lambda or anonymous function

# def func(a):
#  return a**2

# result= func(5)
# print(result)





##another method 

def func(a):
 return a**2

square= func # assining the function in a variable
result= square(7)
print(result)




## important concept- lambda function

fun = lambda num: num ** 2
resultt = fun(4)
print(resultt)

# some more examples

divide = lambda x: x / 2
print(divide(5))        # 25
print(float(divide(5)))


dividetogetint = lambda x: int(x / 2)
print(dividetogetint(9)) #4


add = lambda a, b: a + b
print(add(3, 4))        # 7


multiply = lambda x, y: x * y
print(multiply(6, 8))   # 48



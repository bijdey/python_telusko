#525

# def divide (a,b):
#   if a>b:
#     return a/b
#   else:
#     return b/a

# result= divide(4,2)
# print(result)
# resu= divide(4,6)
# print(resu)






##note this can be done by swaping

def divide(a,b):
  if b>a:
    a,b= b,a
  return a/b
result= divide(5,6)
res= divide(4,2)
print(result, res)


def sub(a,b):
  if b>a:
    a,b= b,a

  return a-b
sres= sub(2,5)
ssres =sub(9,2)
print(sres, ssres)





## just learn about the decorator

# def greater_first(func):
#     def wrap(a, b):
#         if a < b:
#             a, b = b, a      # Swap so the larger number is first
#         return func(a, b)    # Call the original function
#     return wrap


# @greater_first
# def divide(a, b):
#     return a / b


# result = divide(5, 6)
# res = divide(4, 2)
# print(result, res)


# @greater_first
# def sub(a, b):
#     return a - b


# sres = sub(2, 5)
# ssres = sub(9, 2)
# print(sres, ssres)



##use the another syntax important
def greater_first(func):
    def wrap(a, b):
        if a < b:
            a, b = b, a      # Swap if first number is smaller
        return func(a, b)    # Call the original function
    return wrap


# ------------------ Divide ------------------

def divide(a, b):
    return a / b

divide = greater_first(divide)

result1 = divide(5, 6)
result2 = divide(4, 2)

print(result1, result2)


# ------------------ Subtract ------------------

def sub(a, b):
    return a - b

sub = greater_first(sub)

result3 = sub(2, 5)
result4 = sub(5, 1)

print(result3, result4)






def log_deco(func):

    def wrap(a, b):
        print("Values:", a, b)

        result = func(a, b)
        print("Result:", result)

        return result

    return wrap


def add(a, b):
    return a + b


add = log_deco(add)

result1 = add(4, 8)

print(result1)
      
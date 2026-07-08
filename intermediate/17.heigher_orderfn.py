#451
# A Higher-Order Function is a function that takes another function as an argument or returns another function.


# ===========================================
# HIGHER-ORDER FUNCTION (HOF)
# ===========================================

# Definition:
# A Higher-Order Function is a function that:
#
# 1. Takes another function as an argument.
#                OR
# 2. Returns another function.
#
# In Python, functions are treated like variables.
# This means we can:
# - Store a function in a variable.
# - Pass a function to another function.
# - Return a function from another function.


# -------------------------------------------
# Step 1: Create some normal functions
# -------------------------------------------

def square(num):
    return num * num


def cube(num):
    return num * num * num


# -------------------------------------------
# Step 2: Create a Higher-Order Function
# -------------------------------------------

def operate(num, operation):

    # 'operation' is a function.
    # We call it by writing:
    # operation(num)

    return operation(num)


# -------------------------------------------
# Step 3: Pass a function as an argument
# -------------------------------------------

result = operate(5, square)  ## here what is happeing is square(5)
print(result)

# Output:
# 25


result = operate(5, cube) ## here what is happeing is cube(5)
print(result)

# Output:
# 125


# ===========================================
# How it works
# ===========================================

# operate(5, square)
#
# num = 5
# operation = square
#
# return operation(num)
#
# becomes
#
# return square(5)
#
# becomes
#
# return 25


# ===========================================
# IMPORTANT
# ===========================================

# We write:
# operate(5, square)
#
# NOT
#
# operate(5, square())
#
# Why?
#
# square   -> Passes the FUNCTION itself.
# square() -> Calls the function immediately
#             and passes its RETURN VALUE.


# ===========================================
# Easy Trick to Remember
# ===========================================

# Imagine:
#
# operate() = Manager
#
# square()  = Employee 1
# cube()    = Employee 2
#
# The manager doesn't know how to do the work.
# It simply gives the work to whichever employee
# you pass to it.

# operate(5, square)
# Manager -> "Square, do this."

# operate(5, cube)
# Manager -> "Cube, do this."

# Same manager.
# Different employee.
# Different result.
#this topic is not to important but needs to be logical understandable

# def outer():
#   print('in outer function')
#   def inner():
#     print('in inner function')

# outer() #in outer function
# inner() # if i call inner i will get this NameError: name 'inner' is not defined, we can't call the inner function directly because it is inside a function


#let's call the inner function 

# def outer():
#   print('in outer function')
#   def inner():
#     print('in inner function')
#   inner()

# outer() #in outer function.  in inner function










#this is the main concept

 
# ==========================================================
#            NESTED FUNCTIONS IN PYTHON
# ==========================================================

# A nested function is a function defined inside another function.
# The inner function can only be accessed from within the outer function.


def outer():
    # Step 1: This executes when outer() is called.
    print("In outer function")

    # Step 2: Define the inner function.
    # At this point, Python only creates the function.
    # It is NOT executed yet.
    def inner():
        print("In inner function")

        # No return statement is written here.
        # Therefore, Python automatically returns None.

    # Step 3: Call the inner function.
    # Because of (), inner() executes immediately.
    # Whatever inner() returns is returned by outer().
    return inner()


# ==========================================================
# Calling the outer function
# ==========================================================

# outer() is executed.
# The returned value is stored in the variable "something".
something = outer()


# ==========================================================
# Printing the returned value
# ==========================================================

print(something) #In outer function. In inner function. None
print(type(something)) #<class 'NoneType'>
print(something is None) # True
# =========================
# OUTPUT
# =========================
# In outer function
# In inner function
# None


# =========================
# EXECUTION FLOW
# =========================
# outer() is called
#      ↓
# Prints "In outer function"
#      ↓
# inner() is created
#      ↓
# return inner() calls inner()
#      ↓
# Prints "In inner function"
#      ↓
# inner() returns None (no return statement)





##so how we wil get the value instead of none, VVIP concept


# ==========================================================
#        RETURNING A FUNCTION WITH ARGUMENTS
# ==========================================================

def outerr():
    print("In outerrr function")

    # innerr() accepts one parameter: num
    def innerr(num):
        print("Number =", num)

    # Return the function (don't execute it)
    return innerr


# outerr() executes.
# It prints "In outerrr function".
# It returns the innerr function.
somethingg = outerr()


# somethingg now refers to innerr().
#
# somethingg
#     │
#     ▼
# innerr(num)

# Calling somethingg(5) is actually the same as:
#
# innerr(5)
#
# Python automatically passes:
#
# num = 5
#
# So the function executes:
#
# print("Number =", num)

somethingg(5)


# ==========================================================
# OUTPUT
# ==========================================================

# In outerrr function
# Number = 5


# ==========================================================
# EXECUTION FLOW
# ==========================================================

# 1. outerr() is called.
#
# 2. Prints:
#    In outerrr function
#
# 3. innerr(num) is created.
#
# 4. return innerr
#    Returns the function object.
#
# 5. somethingg stores the innerr function.
#
# 6. somethingg(5)
#       ↓
#    innerr(5)
#
# 7. Python assigns:
#
#    num = 5
#
# 8. Executes:
#
#    print("Number =", num)


# ==========================================================
# EASY TRICK TO REMEMBER
# ==========================================================

# def innerr(num):
#
# 'num' is just a placeholder (parameter).
#
# When you call:
#
# somethingg(5)
#
# Python matches:
#
# 5  ---> num
#
# Example:
#
# somethingg(10)  --> num = 10
# somethingg(25)  --> num = 25
# somethingg(100) --> num = 100
#
# The value inside () is always assigned to the parameter.




#another example 
def out_err(num):
    print("In out_errr function:", num)

    def in_nerr(num):
        print("In in_nerrr function:", num)

    return in_nerr


somethingg = out_err(10)

somethingg(5) # In outerrr function: 10. In innerrr function: 5
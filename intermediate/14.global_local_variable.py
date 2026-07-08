#422

a= 10
def something():
  
  print("inside: ", a) 


something() #inside:  10

print('outside: ',a) #outside:  10





##diff example 

b= 90
def anothersomething():
  b= 80
  print("inside: ", b) 


anothersomething() #inside:  80

print('outside: ',b) #outside:  90





c= 7
def ansomething():
  print(globals())
  print(globals()['c']) # 7
  c=8
  print('inside fn: ', c)  #inside fn:  8

ansomething()

print('outside fn: ', c) #outside fn:  7




## change of the global variable

d= 10
def anothsomething():
  globals()['d']= 20 # changing the global variable this variable will be accessed outside the function
  d= 15
  print('inside: ', d) # 15

anothsomething() 
print('outside: ', d) #20





# ============================
# IMPORTANT CONCEPT:
# Local Variable vs Global Variable
# ============================

# Global variable
e = 88

def esomething():

    # This creates a LOCAL variable named 'e'.
    # It exists only inside this function.
    e = 99

    # globals() returns the dictionary of all global variables.
    # This line changes the GLOBAL variable 'e' from 88 to 77.
    globals()['e'] = 77

    # Python always looks for local variables first.
    # Since a local 'e' exists, it prints 99 instead of 77.
    print("Inside:", e) 

# Function call
esomething() #99

# Outside the function, there is no local variable.
# Therefore, Python prints the GLOBAL variable,
# which was changed to 77 using globals().
print("Outside:", e) #77


# ----------------------------
# OUTPUT
# ----------------------------
# Inside: 99
# Outside: 77
#
# Why?
#
# Local Scope
# -----------
# e = 99
#
# Global Scope
# ------------
# e = 77
#
# The local variable hides (shadows) the global variable
# inside the function.
#
# Rule to Remember:
#
# 1. Local variables have higher priority than global variables.
# 2. globals()['e'] changes ONLY the global variable.
# 3. It does NOT change the local variable having the same name.
# 4. If a local variable exists, Python uses it first.

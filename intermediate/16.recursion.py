###recursion is a function calling itself

import sys
from time import sleep
# Print the default recursion limit
#print("Default limit:", sys.getrecursionlimit())

# Change the recursion limit
sys.setrecursionlimit(5000)

# Print the updated recursion limit
print("New limit:", sys.getrecursionlimit())





def greet():
  print('hello')
  greet()
  

#greet()



count= 1
## let's see an example
def hello():
  global count
  print('hello', count)
  count+= 1
  sleep(0.03)
  hello()

#hello()




###factorial of a number using the recursion

def fact(num):

    # Base Case
    # When num becomes 0, stop the recursion.
    # 0! = 1
    if num == 0:
        return 1

    # Recursive Case
    # Multiply the current number with the factorial
    # of the previous number.
    return num * fact(num - 1)


result = fact(5)
print(result)


  
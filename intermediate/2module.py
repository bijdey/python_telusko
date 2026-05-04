##2:36
 ## as we know there are many modules in which math is also a module
import math 


num = 25
result = math.sqrt(num)      # Returns float: 5.0
res = int(math.sqrt(num))    # Converts to int: 5
print(result, res, sep=', ') # ✅ Output: 5.0, 5



## what if i want to import few things from a certain module

#from math import sqrt
#print(sqrt(35)) #5.916079783099616



##float comes to lower integer and ceil go to heiger integer 

print(math.floor(23.1), math.ceil(23.1), sep=', ') # 23, 24
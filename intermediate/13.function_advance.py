##409 

def add(n1,n2=0):  ## default arguments, if not given it will take zero
  return n1+ n2

result= add(4,5)
result2= add(4)
print(result, result2)  #9 4


## variable length arguments to take multiple argument at once
def addition(n1, *n2):
    sum = n1
    for num in n2:      # num is the actual value
        sum += num      # Add the value directly
    return sum

result = addition(2, 34, 45, 5)
result1= addition(9)
print(result, result1)  # Output: 86 9




## keyword argument
def person(name, age):
   print("name:", name)
   print("age:", age)
person('bijay', 25) #name: bijay age: 25

person(age= 22, name= 'kusum') #name: kusum age: 22





##keyword length agrument

def data(name, **kwargs):  # **kwargs collects key-value pairs as dictionary
    print(name)
    print(kwargs)
    
    # Loop through the dictionary
    for i, j in kwargs.items():
        print(i, ':', j)

data(name='bijay', age=25, loc='delhi', stack='MERN')
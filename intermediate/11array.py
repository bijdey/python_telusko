
## 3:58
from array import *

## note that one array has only one type of data, 
# so we cannot store different types of data in one array

arr1= [33, 4, 55, 89 ,12]
print(type(arr1)) #output: <class 'list'>

arr2= array('i', [33, 4, 55, 89 ,12])
print(type(arr2)) #output: <class 'array.array'>
print(arr2) #array('i', [33, 4, 55, 89, 12])
print(arr2.tolist()) #[33, 4, 55, 89, 12]
print(arr2.buffer_info())


for n in arr1:
    print(n)  #this will print the value one by 
    




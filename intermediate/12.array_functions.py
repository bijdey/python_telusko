from array import array

arr1 = array('i', [23, 43, 534, 89])
print(arr1) #array('i', [23, 43, 534, 89])

arr1.append(99)# append changes the original array 
print(arr1) #array('i', [23, 43, 534, 89, 99])
for i in arr1:
    print(i) # print from 23 to 99 one by one in next line

print(arr1.reverse()) #None
# reverse() modifies array in-place and returns None, so print(arr1.reverse()) prints None; 
# use arr1.reverse() then print(arr1) or print(arr1[::-1]) for new reversed array

arr1.reverse
print(arr1) #array('i', [99, 89, 534, 43, 23])




## another concept
##arr1= array('i', [99, 89, 534, 43, 23])
# arr2 = arr1 does NOT create a new array - both variables point to the SAME array object in memory
# Any modification to arr1 will also affect arr2 (and vice versa) because they reference the same object

arr2 = arr1  # Both arr1 and arr2 point to the same memory location
print(arr1, arr2)  # Same output: array('i', [99, 89, 534, 43, 23]) array('i', [99, 89, 534, 43, 23])

arr1[2] = 4  # Modifying arr1 also changes arr2
print(arr1, arr2)  # Both show: array('i', [99, 89, 4, 43, 23]) array('i', [99, 89, 4, 43, 23])





##concept of coping an array to a new variable

arrx= array('i', [43, 2, 54, 645])
arry=array(arrx.typecode, arrx.tolist()) #here a new array is formed, note here more memory is used becasue a list is formed

print(arrx, arry) #array('i', [43, 2, 54, 645]) array('i', [43, 2, 54, 645])


## the best way to do is means copy an array is see below

arra= array('i',[ 534, 32, 23, 32423,])
arrb= array(arra.typecode, (n for n in arra))
print(arra, arrb)
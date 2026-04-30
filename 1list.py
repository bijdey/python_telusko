##list is mutable and we can change the values

nums=[56, 43, 32, 53, 23, 67, 78]

print(nums)

print(len(nums))

#slicing

print(nums[2:4])  #last value is excluded

name= ['bijay', 'kumar', 'pandey']

mix= ['bijay', 25, 5.9]

mixture=[nums, name]
print(mixture)  #[[56, 43, 32, 53, 23, 67, 78], ['bijay', 'kumar', 'pandey']]

print(mixture[0][1]) #43
print(mixture[-1][-1]) #pandey

#single list haveing all the values
combinelist= nums + name
print(combinelist) #[56, 43, 32, 53, 23, 67, 78, 'bijay', 'kumar', 'pandey']


#as of now nums is [56, 43, 32, 53, 23, 67, 78, 3]
nums.append(3) # it add the value at the end, and modify the existing list
print(nums)

count= nums.count(32) #it counts that how many times the value appear
print(count)  #1

nums.insert(1,88) # first is the index of the new value of second element(value which is 88)

print(nums) #[56, 88, 43, 32, 53, 23, 67, 78, 3]

nums.remove(67)
print(nums) #[56, 88, 43, 32, 53, 23, 78, 3]


no=[34, 77, 23, 90, 45, 89 ]

# if index is not given then last element deleted,
no.pop()
print(no) #[34, 77, 23, 90, 45]

#pop takes index value and remove the element present on that index
no.pop(2)
print(no) #[34, 77, 90, 45]


#del takes two index to delete and end not included

del no[1:3]
print(no) #[34, 45]


list= [ 8,2,5]

## want to insert multiple values
list.extend([34,23,353,4323])
print(list) #[8, 2, 5, 34, 23, 353, 4323]


##replace values in list using index end not included

list[2:4]= [89,90]
print(list) #[8, 2, 89, 90, 23, 353, 4323]




##reverse the list
data= [18, 12, 89, 90, 23, 353, 4323]


data.reverse()
print(data) #[4323, 353, 23, 90, 89, 12, 18]

##sort in assending order
data.sort()
print(data) #[12, 18, 23, 89, 90, 353, 4323]

#to find the minium and maximum number

print(min(data)) #12
print(max(data)) #4323

print(min(data), max(data), sep=", ")


print(sum(data))



namees= ['karan', 'bijay', 'harsh', 'rohit', 'yaman', 'rahul', 'raman', 'aman', 'ajmal']

print(min(namees)) #ajmal







##A set is an unordered collection of unique elements.

set1= {23, 56, 78, 21, 56}
print(type(set1)) #<class 'set'>

print(set1) #{56, 21, 78, 23}, it stores based in hash value, 
            #because it helps to speed the process in saving and fetching

print(23 in set1) #true
print(len(set1)) #4 (it counts unique elements)

#how to assign empty set

set2={}
print(type(set2)) #<class 'dict'>


set3=set()
print(type(set3)) #<class 'set'>



setA=set('abccdmnnnop')
setB=set('aeioupddd')
print(setA) #{'c', 'n', 'o', 'p', 'm', 'd', 'a', 'b'}
print(setB) #{'i', 'u', 'e', 'o', 'p', 'd', 'a'}

print(setA-setB) #{'m', 'b', 'c', 'n'}

print(setA | setB) #{'i', 'a', 'n', 'p', 'm', 'u', 'o', 'e', 'c', 'd', 'b'} 

print( setA & setB) #which are common # {'d', 'a', 'p', 'o'}
 
print( setA ^ setB) #which are not common #{'b', 'c', 'u', 'n', 'm', 'e', 'i'}
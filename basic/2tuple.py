##tupple is immutable we can't cahnge the values
list=[23,54,76,54,43]
print(type(list))#<class 'list'>


tup= 23,54,76,54,43
print(type(tup)) #<class 'tuple'>


tupp= (23,54,76,54,43)
print(type(tupp)) #<class 'tuple'>

##if there is only single value present its type will be intezer
tuppp= 43
print(type(tuppp)) #<class 'int'>


##min max sum etc, works in the tupple as well same as list


tuple= 3, 6, 23, 543

print(tuple[2]) #23

print(len(tuple)) #4




tupA= 5, 'bijay', 4.89

num, name, decnum= tupA
print(name) #bijay




# we can't replace any element of the tuple as it is not mutable
# tupA= 5, 'bijay', 4.89

# tupA[1]= 5
# print(tupA) #TypeError: 'tuple' object does not support item assignment




# as we cant change the element of the tuple, but yes we can change the element present in the element of the tupple 
# for example the list is inside the tuple, we can't replace or change the list, but yes we can change the element of the list

tupB= 43, 'pandey', [5,6,7,8,9]

tupB[2][1]=45
print(tupB) #(43, 'pandey', [5, 45, 7, 8, 9])


tupN= 54, 75, 'kumar', 45.43
print(75 in tupN) #True


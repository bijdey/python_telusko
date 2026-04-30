## note that each time you will run each time the memory identical place will get changed


a= 5
b= 5
## as the value 5 has same adress and a and b are only refrances
print(id(a)) #140730051482872, the identity or adress or a
print(id(b)) #140730051482872, the identity or adress or b



b= 6
##now it's value changes because it's adress changes, as 6 has different adress, but we 
#already know that b is only refrance, so we don't need to think about b 
print(id(b)) #140730051482904, the identity or adress or b




fname= 'bijay'
name='bijay'
lname= 'pandey'

print(id(fname)) # 2217173586576
print(id(name))  # 2217173586576
print(id(lname))  # 2217173586512



##here as the string is large so the adress may be same or may not be same,
#mostly not same
a= 'my fav color is black and i like to eat mangoes'
b= 'my fav color is black and i like to eat mangoes'

print(id(a))
print(id(b))


##here same they may not come same and they may come same
n=10000000000000898097465468744216587987987
m=10000000000000898097465468744216587987987

print(id(n))
print(id(m))
506

# nums=[4, 3, 56, 67, 89, 2, 43, 88, 95]
# even= []
# for i in nums:
#   if(i %2 == 0):
#     even.append(i)
#     print(i)

# print(even)



## another way of doing the same is the filer

# nums=[4, 3, 56, 67, 89, 2, 43, 88, 95]
# def is_even(n):
#   if n%2 ==0:
#    return True


# even= list(filter( is_even , nums))
# print(even)




#doing the same thing using lambda function and this is important

# nums=[4, 3, 56, 67, 89, 2, 43, 88, 95]
# is_even= lambda n: n%2==0

# even= list(filter(is_even, nums))
# print(even)

# now to make this in one line we can use this

nums=[4, 3, 56, 67, 89, 2, 43, 88, 95]
even= list(filter(lambda n: n%2==0, nums))
print(even)






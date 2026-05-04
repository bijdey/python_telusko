##2:59



# num=6

# #note: in first block odd is inside the if, here both will be printed as by default things are true and no logic is given
# # in second block odd is outside the if, here also both will be printed 
# # in third block hello is outside the if, here only hello will be printed 

# ##so the main learning is that the spaces and tabs are importent in if and else block
# if True:
#     print('Even')

#     print('Odd')

# if True:
#     print('Even')

# print('Odd')


# if False:
#     print('Even')
# print('hello')





##########

num= 35

if num%2==0:  # we can also write like this if (num%2==0)
    print('Even number')
else:
    print('Odd number')

print('bye')



######
######


## nested if

sal=22
if sal%2==0:
    if sal>=5:
        print('great job')
    else:
        print('better luck next time')
else:
    print('odd salary')
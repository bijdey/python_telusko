
for val in range(10):
  print(val)

##
####
#what if we need to skip the val divisible by 3

for value in range(10):
  if value %3 != 0:
    print(value) #kindly note that this value is inside the if block



## another way to do the same thing

##how the continue works we can see the example
for valu in range(10):
  if valu % 3==0:
    continue    ## here what continue does is that if any value is found which is divisible by 3 it continues means it does nothing means it skips and goes to the next value, and in this was we can print the val outside the if block but inside the for block
  print(valu)






###################
#what if i want to only less than 5
for data in range(10):
  if data<5:
    print(data)

## here is the example how the break works the same example as above

for num in range(10):
  if num== 5:
    break  ## here break will, break the loop until this condition is reached
    print(num)


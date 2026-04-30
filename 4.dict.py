

data={
    0: 342,
    1: 344,
    2: 988,
    3: 7878,
    4: 892
}

print(data[3]) #7878,  kindly note that 3 is not an index, it is a key

dataa={
    'bijay': 342,
    'karan': 344,
    'harsh': 988,
    'aman': 7878,
    'raju': 892
}

print(dataa['bijay']) #342

print(dataa.get('bijay')) #342

print(dataa.get(1)) #None, as not able to find any key (don't ever thing that it is a index)

print(dataa.get('gaurab', 'not found')) #not found



##The Key Rule: Dictionaries cannot have duplicate keys..
# When you create a dictionary, each key must be unique. If you use the same key twice,
#  the second occurrence OVERWRITES the first., as you can see raju came twice so the
#second one overwrites the first.

info={
    'bijay': 342,
    'karan': 344,
    'harsh': 988,
    'aman': 7878,
    'raju': 892,
    'raju': 200
}

print(info) #{'bijay': 342, 'karan': 344, 'harsh': 988, 'aman': 7878, 'raju': 200}



##integrate key and value to form dictionary

keys=['orange', 'red', 'pink']
values=[23, 534, 432]
dict1=dict(zip(keys,values))

print(dict1) #{'pink': 23, 'orange': 534, 'red': 432}


# now here the sequence is not maintained, as we use curely brases
keys={'orange', 'red', 'pink'}
values=[23, 534, 432]
dict1=dict(zip(keys,values))

print(dict1) #{'pink': 23, 'orange': 534, 'red': 432}




data={'kiran': 34, 'sushil': 30, 'raman': 90, 'yash': 56}

print(data.pop('sushil')) #30, it tell the value of the key as well as it modify the existing set by deleting the key and value pair
print(data) #{'kiran': 34, 'raman': 90, 'yash': 56}

del data['raman']  # ✅ No print, just delete, as it modifies the existing set

print(data)  # {'kiran': 34, 'yash': 56}                                   


lang={
    'js': 'vscode',
    'python': ['vscode', 'pycharm'],
    'java': {'core':'vscode', 'spring': 'iij'}
}
print(lang)

print(lang['js']) #vscode
print(lang['java']['spring']) #iij



import os
import re
fileOpen = open('software_Centre', 'r')
filePrint = fileOpen.readlines()
print("Text to dict")
print(filePrint)

dict1 = {}
for dictIter in filePrint:
    (key, value) = dictIter.split()
     dict1[key] = value
    
print(dict1)
print(type(dict1))
print("Searching ...")
res = None
for key in dict1.keys():
    if 'python' in key:
        res = key
        break
print('Software: {} Version: {}'.format(key, dict1[key]))

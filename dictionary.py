__author__ = 'iWanjugu'

#syntax:
    #name = {keys:value}

classmates = {'Tony': ' cool but smells', 'Emma': ' sits behind me', 'Lucy': ' Asks too many questions'}

print (classmates)
print(classmates ['Emma'])

#looping through dictionaries

for k,v in classmates.items(): #two placeholders 'k' for keys and 'v' for value; .items function/extension
    print (k + v)
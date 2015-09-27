__author__ = 'iWanjugu'
foods = ['bacon', 'tuna', 'ham', 'fruits', 'beef']

# syntax :
# for f(placeholder variable) in foods(variable you want to go through):
    #your function/ method/ what you want to do many times

for f in foods:
    print (f)
    #can perform multiple tasks inside the same for loop
    #make sure it's indented at the same level with the previous command (??????)
    print(len(f))

#with just a part of the list
for f in foods [:2]: #just looks at bacon and tuna
    print (f)
    print(len(f))
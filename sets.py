__author__ = 'iWanjugu'

#a collection of items but can't have any duplicates

groceries = {'cereal', 'milk', 'eggs', 'bread', 'eggs'}
print(groceries) #only prints 'eggs' once

if 'milk' in groceries:
    print("You already have milk!")
else:
    print("You need milk!")
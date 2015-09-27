__author__ = 'iWanjugu'
# single line comment
"""
multiple
line
comment
"""


#concatenating string and number - use ',' instead of '+'
print (9, "Bucky")

magicNumber = 26

for n in range (101): #looking through 0 -100 to check ifour magic number is in there
    if n is magicNumber:
        print(n, " is the magic number!")
        break #stops the loop - no need to continue the loop after finding what you're looking for
    else:
        print(n) #prints all numbers up to the magic number
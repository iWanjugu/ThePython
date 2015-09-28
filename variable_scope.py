__author__ = 'iWanjugu'
#Variables that a function is allowed/able to use


a = 7823

def corn():
    print(a)

def fudge():
    print(a)

corn()
fudge() #both variables can access 'a' since it's been created OUTSIDE any function



def corn():
    b= 7823
    print(b)

def fudge():
    print(b) #fudge cannot print 'b'; The variable has been created inside another function

corn()
fudge()
__author__ = 'iWanjugu'
#defining a function syntax
#def var_name():

def beef ():
    print("Daaaaayum!!!")


def bitcoin_to_usd(btc):
    #formula
    amount = btc * 527
    print(amount)

#calling functions
beef()
bitcoin_to_usd (3.85)



#Function with retrn values

def allowed_dating_age(my_age):
    boys_age = my_age*1.3
    return boys_age #specify which variable you want to be 'returned'

the_limit = allowed_dating_age(27)
sue_limit = allowed_dating_age(24)
print ("I can date boys", the_limit, "or_younger")
print ("Sue can date girls", sue_limit, "or_younger")

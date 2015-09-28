__author__ = 'iWanjugu'
def sentence(name="Irene", action='ate', item='tuna'):
    print(name, action, item)

sentence() #without passing any parameters into the arguments the funtion will use the default set parameters

sentence("Sue", "Farts", "not so gently") #parameters are passed in order

#passing parameters NOT in order; in whatever order you want 
sentence (item="awesome", action="is")
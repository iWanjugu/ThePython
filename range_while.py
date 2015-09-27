__author__ = 'iWanjugu'

#When we don't have a particular variable we want to loop through
#maybe we want to loop through like 10 times
######## use 'RANGE' function


#prints out Variable ('food rocks') 2 times
for x in range(2):
    print ('food rocks')


# prints out a range of numbers (5 to 12) increment = 1
for x in range(5,12):
    print (x)

#prints out a range of numbers with these specifications:
# range (start, end position, increment)
for x in range(10, 40, 5):
    print(x)


######### WHILE LOOP

crack = 5
while crack < 10:
    print(crack)
    crack += 1 #adds 1 to the variable each time. Without this an infinite loop is created
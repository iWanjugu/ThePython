__author__ = 'iWanjugu'

numbersTaken = [2,5,12,13,17]

#we want all the numbers form 1 - 20 without the above ones
print (" Here are the numbers that are still available")
for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)

#unlike break which stops the loop altogether,
# continue skips the number that has been found and continues the loop
__author__ = 'iWanjugu'
# When you do not know how many variables your function will take eg calculator

def add_numbers(*args):
    # (*) signals python to create space for n number of arguments
    # args - can be any name but it is common practice to use args for the flexible variables
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(3, 32)
add_numbers(3, 32, 67, 78)


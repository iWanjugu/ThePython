Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>
user = "Tuna McFish"
>>> #getting first letter
>>> user [0] # 0 is the first position, not 1
'T'
>>> user [5]
'M'
>>> user [-1] #you can start from the last lerre instead
'h'
>>> user[-5]
'c'
>>>
user [2:7] #select from string at position 2 to string in position 7
'na Mc'
>>> user[:7]
'Tuna Mc'
>>>
>>> user [5:] #without the last number - will selet till the end
'McFish'
>>> user [:] #prints out everything
'Tuna McFish'
>>> #Length of a string using function 'len'
>>> len ('hahoeuohgohsjdno')
16
>>> len (user)
11
>>> #blank space is a character
>>>

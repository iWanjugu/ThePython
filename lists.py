Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
players = [29,58,66,71,87] #a list of numbers; starts prom position 0
>>> players [2]
66
>>> #changing an item in a list t another item
>>> players[2] = 68
>>> players # call the varialble players
[29, 58, 68, 71, 87]
>>> #adding items to the end of the list
>>> players + [90,56,40,50]
[29, 58, 68, 71, 87, 90, 56, 40, 50]
>>> players
[29, 58, 68, 71, 87]
>>> # the original players list doesn't change permanently
>>>  #to change or add permanently you use the .append() funtion
>>> players.append(120)
>>> players
[29, 58, 68, 71, 87, 120]
>>> 
#slicing items from the list (similar to the strings)
>>> players [:2]
[29, 58]
>>> players [:2] = [0, 0] #replacing multiple values at once
>>> players
[0, 0, 68, 71, 87, 120]
>>> 
>>> #removing items fron the list
>>>  players [:2] = []
 
SyntaxError: unexpected indent
>>> players [:2] = []
>>> #deleting the entire list
>>> players [:] = []
>>> players
[]
>>> 

"""
Tuple
    Tuples are used to store multiple items in a single variable.
    Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
    A tuple is a collection which is ordered and unchangeable.
    Tuples are written with round brackets.
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)




"""
Tuple Items
    Tuple items are ordered, unchangeable, and allow duplicate values.
    Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
    
    Ordered
        When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

    Unchangeable
        Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

    Allow Duplicates
        Since tuples are indexed, they can have items with the same value.
"""
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)




"""
Tuple Items - Data Types
    Tuple items can be of any data type.
"""
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")




"""
Create Tuple With One Item
    To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
"""
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))




"""
Tuple Length
    To determine how many items a tuple has, use the len() function
"""
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))




"""
Access Tuple Items
    You can access tuple items by referring to the index number, inside square brackets.   
    Negative indexing means start from the end. 
    You can specify a range of indexes by specifying where to start and where to end the range.
    When specifying a range, the return value will be a new tuple with the specified items.
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])




"""
Add Items
    Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.
        1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
        2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple.

Remove Items
    Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)




"""
Tuple Methods
    Python has two built-in methods that you can use on tuples.

    Method	    Description
    count()	    Returns the number of times a specified value occurs in a tuple
    index()	    Searches the tuple for a specified value and returns the position of where it was found
"""
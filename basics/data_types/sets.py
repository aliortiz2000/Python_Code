"""
Set
    Sets are used to store multiple items in a single variable.
    A set is a collection which is unordered, unchangeable*, and unindexed.
    Sets are written with curly brackets.
"""
thisset = {"apple", "banana", "cherry"}
print(thisset)




"""
Set Items
    Set items are unordered, unchangeable, and do not allow duplicate values.

    Unordered
        Unordered means that the items in a set do not have a defined order.
        Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

    Unchangeable
        Set items are unchangeable, meaning that we cannot change the items after the set has been created.
        Once a set is created, you cannot change its items, but you can remove items and add new items.
        
    Duplicates Not Allowed
        Sets cannot have two items with the same value.
"""
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)




"""
Get the Length of a Set
    To determine how many items a set has, use the len() function.
"""
thisset = {"apple", "banana", "cherry"}
print(len(thisset))




"""
Set Items - Data Types
    Set items can be of any data type.
    A set can contain different data types.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}




"""
Access Items
    You cannot access items in a set by referring to an index or a key.
    But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
"""
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)




"""
Join Two Sets
    There are several ways to join two or more sets in Python.
    You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another.
"""
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)




"""
Keep ONLY the Duplicates
    The intersection_update() method will keep only the items that are present in both sets.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)




"""
Keep All, But NOT the Duplicates
    The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
    The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)




"""
Set Methods
    Python has a set of built-in methods that you can use on sets.

    Method	                        Description
    add()	                        Adds an element to the set
    clear()	                        Removes all the elements from the set
    copy()	                        Returns a copy of the set
    difference()	                Returns a set containing the difference between two or more sets
    difference_update()	            Removes the items in this set that are also included in another, specified set
    discard()	                    Remove the specified item
    intersection()	                Returns a set, that is the intersection of two other sets
    intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
    isdisjoint()	                Returns whether two sets have a intersection or not
    issubset()	                    Returns whether another set contains this set or not
    issuperset()	                Returns whether this set contains another set or not
    pop()	                        Removes an element from the set
    remove()	                    Removes the specified element
    symmetric_difference()	        Returns a set with the symmetric differences of two sets
    symmetric_difference_update()	inserts the symmetric differences from this set and another
    union()	                        Return a set containing the union of sets
    update()	                    Update the set with the union of this set and others
"""

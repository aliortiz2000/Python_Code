"""
List
    Lists are used to store multiple items in a single variable.
    Lists are created using square brackets:
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)




"""
List Items
    List items are ordered, changeable, and allow duplicate values.
    List items are indexed, the first item has index [0], the second item has index [1] etc.

    Ordered
        When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
        If you add new items to a list, the new items will be placed at the end of the list.
        
    Changeable
        The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

    Allow Duplicates
        Since lists are indexed, lists can have items with the same value.
"""

"""
List Length
    To determine how many items a list has, use the len() function
"""
thislist = ["apple", "banana", "cherry"]
print(len(thislist))




"""
List Items - Data Types
    List items can be of any data type
    A list can contain different data types
"""
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]




"""
Access Items
    List items are indexed and you can access them by referring to the index number.
    Negative indexing means start from the end.
    Remember that the first item has index 0.
"""
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])




"""
Range of Indexes
    You can specify a range of indexes by specifying where to start and where to end the range.
    When specifying a range, the return value will be a new list with the specified items.
    The search will start at index 2 (included) and end at index 5 (not included):
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])




"""
Check if Item Exists
    To determine if a specified item is present in a list use the in keyword:
"""
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")




"""
List Methods
    Python has a set of built-in methods that you can use on lists.
    
    Method	    Description
    append()	Adds an element at the end of the list
    clear()	    Removes all the elements from the list
    copy()	    Returns a copy of the list
    count()	    Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	    Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	    Removes the element at the specified position
    remove()	Removes the item with the specified value
    reverse()	Reverses the order of the list
    sort()	    Sorts the list
"""

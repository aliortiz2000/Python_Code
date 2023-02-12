"""
Dictionary
    Dictionaries are used to store data values in key:value pairs.
    A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
    Dictionaries are written with curly brackets, and have keys and values.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)




"""
Dictionary Items
    Dictionary items are ordered, changeable, and does not allow duplicates.
    Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
    
    Ordered or Unordered?
        As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
        When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
        Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

    Changeable
        Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

    Duplicates Not Allowed
        Dictionaries cannot have two items with the same key.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)




"""
Dictionary Items - Data Types
    The values in dictionary items can be of any data type.
"""
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}




"""
Accessing Items
    You can access the items of a dictionary by referring to its key name, inside square brackets.
    There is also a method called get() that will give you the same result.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

x = thisdict.get("model")




"""
Get Keys
    The keys() method will return a list of all the keys in the dictionary.
"""
x = thisdict.keys()




"""
Get Values
    The values() method will return a list of all the values in the dictionary.
"""
x = thisdict.values()




"""
Get Items
    The items() method will return each item in a dictionary, as tuples in a list.
"""
x = thisdict.items()




"""
Change Values
    You can change the value of a specific item by referring to its key name.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018




"""
Update Dictionary
    The update() method will update the dictionary with the items from the given argument.
    The argument must be a dictionary, or an iterable object with key:value pairs.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})




"""
Adding Items
    Adding an item to the dictionary is done by using a new index key and assigning a value to it.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)




"""
Removing Items
    There are several methods to remove items from a dictionary.
    The pop() method removes the item with the specified key name.
    The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead).
    The clear() method empties the dictionary.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)




"""
Dictionary Methods
    Python has a set of built-in methods that you can use on dictionaries.

    Method	        Description
    clear()	        Removes all the elements from the dictionary
    copy()	        Returns a copy of the dictionary
    fromkeys()	    Returns a dictionary with the specified keys and value
    get()	        Returns the value of the specified key
    items()	        Returns a list containing a tuple for each key value pair
    keys()	        Returns a list containing the dictionary's keys
    pop()	        Removes the element with the specified key
    popitem()	    Removes the last inserted key-value pair
    setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
    update()	    Updates the dictionary with the specified key-value pairs
    values()	    Returns a list of all the values in the dictionary
"""
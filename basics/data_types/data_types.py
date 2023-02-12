"""
Built-in Data Types

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

- Text Type:	str
- Numeric Types:	int, float, complex
- Sequence Types:	list, tuple, range
- Mapping Type:	dict
- Set Types:	set, frozenset
- Boolean Type:	bool
- Binary Types:	bytes, bytearray, memoryview
- None Type:	NoneType
"""

x = "Hello World"	                            #str
x = str("Hello World")
	
x = 20	                                        #int	
x = int(20)

x = 20.5	                                    #float	
x = float(20.5)

x = 1j	                                        #complex	
x = complex(1j)

x = ["apple", "banana", "cherry"]	            #list	
x = list(("apple", "banana", "cherry"))

x = ("apple", "banana", "cherry")	            #tuple	
x = tuple(("apple", "banana", "cherry"))

x = range(6)	                                #range	

x = {"name" : "John", "age" : 36}	            #dict	
x = dict(name="John", age=36)

x = {"apple", "banana", "cherry"}	            #set	
x = set(("apple", "banana", "cherry"))

x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = frozenset(("apple", "banana", "cherry"))

x = True	                                    #bool	
x = bool(5)

x = b"Hello"	                                #bytes	
x = bytes(5)

x = bytearray(5)	                            #bytearray	
x = bytearray(5)

x = memoryview(bytes(5))	                    #memoryview	
x = memoryview(bytes(5))

x = None	                                    #NoneType
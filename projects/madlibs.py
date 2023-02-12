# String concatenation 

# 

some_string = "Alines Ortiz " # Some string value

# Different ways we can put strings together 
print ("My name is " + some_string)
print ("My name is {}".format(some_string))
print (f"My name is {some_string}")

# The cleanest way to concat strings 
another_string = input("Full Name: ")

madlib = f"I'm {another_string}, a 22 year old female computer engineering student."


# Second example
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
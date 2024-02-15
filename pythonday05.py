#Class and object
# ==============

# object oriented programming (or OOP)
# class = class
# object = object

# A class always has properties and functions
# properties are variables defined in a class
# operations are functions with which class members do something

# class is used to build objects.
# So a class is a model and an object is a single thing created according to the model.
# An object is always separate from another object.
# An object's properties can get new values during its lifetime.
# entities live their own lives independently of other entities.

# Functions (functions) are also defined in the classes.
# This way each separate entity does what it needs to do.
# operation is independent of other objects.
# functions use the internal data of the object to achieve the desired action.
# Functions focus on what the object should be able to do.
# Other functions are not needed and should not be supported.
#from doctest import REPORT_UDIFF

class Personel:
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
    def say_name(self):
      print(f"My name is {self.name}!")

person1 = Personel("Sushila Kandel", 23)
person2 = Personel("John Dimes", 32) 
print(person1.name)
print(person2.name)


person2.name = "Binita Dimes" 
print(person1.name)
print(person2.name)  
person1.say_name()
person2.say_name()     


# The A and O of object-oriented programming is planning
# In principle, all classes must be planned in advance

# Customer class
# It must be able to:
# Search for books
# Borrow and return books
# I'll pay the fines
# --> Each of these things is a function, or functionality

# --> after this we can think about features that support functions
# Eg Book class
# Author
# number of pages
# Publication year
# Name
# ISBN/ISSN number

# the class is defined with the word class

class Animal:
    
    def __init__(self):
        self.name = ""
        
        
pet1 = Animal()
pet1.name = "Sylvi"
print(pet1.name) 
pet2 = Animal()
print(pet2.name) 

class Cat:
    def __init__(self, race, name, gender, age):
      self.race = race
      self.name = name
      self.gender = gender
      self.age = age 
      
# when performing functions, self specifies that own properties can be used

def walks(self):
  print(f"{self.name} is walking")
#functions have parameters

def spin(self, description):
    print(f"The cat is purring {description}")
              
cat1 = Cat("", "Jenny","F",13)
cat1.walks()
cat1.purr("happily")

# two more cats
cat2 = Cat("Katti", "Kali", "M", 16)
cat3 = Cat("Katt","Galileo","M", 16)
cat3.age = 14
cat3.purr("")     

# Collection

# The class may not be able to stretch to everything
# accumulation of functions increases complexity
# handling of special cases and edge cases
#
# --> then collection is used
# --> Collection is used to handle special cases!
#
# --> mother class remains simple
# --> child class handles special case
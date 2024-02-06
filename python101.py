

#101 execise 5 feb 2024
print("My name is Sushila Kandel")

#102 program that prints the following names in alphabetical order:
# "Aarne", "Bertta", "Celsius", "Daavid"

#a = { "Bertta", "Celsius", "Daavid", "Aarne" }
#x = sorted(a)
#print(a)

a = ["Bertta", "Celsius", "Daavid", "Aarne"]
x = sorted(a)
print("Original set:", a)
print("Sorted list:", x)


#103 program with the name "Eemeli" last and "Aapeli" after Aarne

x.insert(4, "Eemeli")
x.insert(1, "Aapeli")
print("Added list:",x)

#104 program that writes the following rhyme:
""" Mä olen olen kotoisin
Hyvinkään getosta.
Jos joku muuta väittää
se on petosta!
"""
def func_rhyme():
  rhyme ="""Mä olen olen kotoisin
Hyvinkään getosta.
Jos joku muuta väittää
se on petosta!"""
  print(rhyme)
func_rhyme()

#105 write a program that calculates the number of hours in a year
#106 Write a program that counts the number of minutes in a year
def funct_hours_in_year():
  days_year = 365
  hours_day = 24
  min_hours = 60
  hours_in_year = days_year*hours_day
  mins_in_year = days_year*hours_day*min_hours
  
  return hours_in_year, mins_in_year
# function call to calculate the result
hours,minutes  = funct_hours_in_year()


print(f"Number of hours in a year: { hours}")
print(f"Number of minutes in a year: { minutes}")

#Exercise 107: Write a program that prints
#Hello, my name is Simo 'Sapeli' Suomalainen!
#Exercuse 108:Write a program that prints print("Hellow world!")
def name_func():
  name = """Hello, my name is Simo 'Sapeli' Suomalainen!"""
  phrase = """print("Hello world!")"""
  print(name)
  print(phrase)
name_func()
  

   
   
   
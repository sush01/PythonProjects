#Python 106

#Tavoite:

#len komento
""" 
sana = "Aku Ankka"
print(len(sana))

tietotyyppien väliset muunnokset
muuttuja = str(1234)
muuttuja = int(5.15)
muuttuja = int("123")
muuttuja = float("123.45")
"""

#Tehtävä 106-1: Tee ohjelma, jossa kirjoitetaan merkkijono ja ilmoitetaan sen pituus.
"""
my_string = input("Enter your string:")
print("Entered string's length is:",len(my_string))
"""


#Tehtävä 106-2: Tee ohjelma, jossa kirjoitetaan liukuluku ja ohjelma ilmoittaa sen pyöristyksen kokonaisluvuksi.

number = 34.00
print("Number is:", int(number))


#Tehtävä 106-3: Tee ohjelma, jolle syötetään luku Celsiusasteina. Ohjelma ilmoittaa arvon Fahrenheitteina. Etsi kaava netistä.
celsius = float(input("Enter number in celsius:"))

fahrenheit = (celsius * 1.8) + 32

print(  " Celsius is equivalent to Fahrenheit is:" ,fahrenheit)
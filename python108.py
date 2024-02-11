#Python 108
"""
and, or ja not

if luku >= 2 and luku <= 4:
    print("Luku on välillä 2 ja 4")
	
"""

#Tehtävä 108-1: Tee ohjelma, joka kysyy luvun ja sanoo että alle 10 on pieni ja että negatiivinen luku on negatiivinen. Muuten luku on suuri.
"""
number = int(input("Enter any number:"))
if number < 10:
    print("Number is small.")
    if number < 0:
        print("Number is negative.")
else:
        print("Number is big.")
    
"""

#Tehtävä 108-2: Tee ohjelma, joka ilmoittaa onko syötetty nimi joku Aku Ankan veljenpojista.

name = input("Enter name: ")
if name == "Tupu" or name == "Hupu" or name == "Lupu":
    print(f"{name} on veljenpoika.")
else:
    print(f"{name} ei ole veljenpoika.")



#Tehtävä 108-3: Tee ohjelma, joka ilmoittaa onko syötetty kokonaisluku jaollinen viidellä.

number = int(input("Enter number:"))

if number % 5 == 0:
    print(f"{number} is divided by 5.")
else: 
    print(f"{number} is not divided by 5.")
#Tehtävä 108-4: Tee ohjelma, joka laskee onko kyseessä karkausvuosi.

year = int(input("Enter year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
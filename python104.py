#Tavoitteet:
#Ymmärtää aritmetiikkaa

#Aritmetiikan loput tekijät
#jako kokonaisluvuilla
#	% modulo
#	** potenssi

#Python 104-1: Laske painoindeksi BMI eli paino jaettuna pituuden neliöllä (pituus metreinä).
"""
print("\nEnter your weight:")
weight = float(input())
print("\nEnter your height:")
height = float(input())
BMI = weight/int(height*height)
print("\nYour BMI is:",BMI)
"""


#Python 104-2: Python kerro minä vuonna synnyit ja laske näin kuinka vanha olet
"""
from datetime import datetime 
print("Enter your birth year:")
birth_year = int(input())
current_year = datetime.now().year
print("Current year is:", current_year)
age = current_year - birth_year
print("Your age is:", age)
"""

#Python 104-3: Kerro nimesi ja minä vuonna synnyit ja kirjoita seuraavaa:
#Nimesi on <nimi> ja olet <X> vuotta vanha.
"""
print("Enter your name:")
name = input()
print("Enter your age:")
age = int(input())
print("My name is" ,name, "and", "I am", age, "years old")
"""
#Python 104-4: Määritä luku ja ilmoita sen potenssi kahteen.
"""
num1 = 3
num2 = 3
power_of_two = num1 ** 2
print("The power of two of",num1, "is",power_of_two)
print("num1 ** num2 evaluates to: ", num1**num2)
"""
#Python 104-5: Määritä kaksi lukua ja laske niiden potenssi.
"""
num1 = 3
num2 = 3
power_of_two = num1 ** 2
print("The power of two of",num1, "is",power_of_two)
print("num1 ** num2 evaluates to: ", num1**num2)
"""
#Python 104-6: Kerro tietokoneelle monta päivää on kyseessä ja laske niiden minuuttien lukumäärä
"""
print("Enter number of days:")
day = int(input())
hours = 24
minutes = 60
result = day * hours * minutes
print("No of minutes of the days entered is:",result)
"""

#Python 104-7: Syötä kolme lukua ja laske niiden tulo

print("Enter 3 numbers:")

a = int (input())
b = int (input())
c = int (input())

product = a * b * c
print("The product of", a,b,c, "is", ":", product)


#Python 104-8: Syötä kolme lukua ja laske niiden summa
sum = a + b + c
print("The sum of", a,b,c, "is", ":", sum)


#Python 104-9: Syötä kolme lukua ja laske niiden keskiarvo
average = (a+b+c)/2
print("The average of", a,b,c,"is",":", average)




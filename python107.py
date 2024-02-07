"""aaa = 123

if a > 200:
	print("200+")
elif a > 100:
	print("100-200")
else:
	print("alle 100")
"""
#Merkkijonoissa voidaan verrata myös aakkosjärjestystä välillä a-z.

#Tehtävä 107-1: Tee ohjelma, joka ilmoittaa monta pistettä tuli jääkiekossa voiton, tasapelin tai tappion tullessa.
"""
def calculate_point(result):
  if result.lower() == "win":
    points = 2
  elif result.lower() == "tie":
    points = 1
  elif result.lower() == "loss":
    points = 0
  else:
    points = None
    print("Invalid result entered")
  return points
    
result = input("Enter the result of the match (win, tie, loss):")
points = calculate_point(result)

if points is not None:
  print("Points scored:", points)
"""

#Tehtävä 107-2: Tee ohjelma, johon syötetään 2 lukua, kerro kumpi on suurempi vai oliko kyseessä sama luku.
"""
def compare(num1,num2):
  if num1 > num2:
    print("Num1 is greater than num2")
  elif num1 < num2:
    print("Num2 is greater than num1")
  else:
    print("Both are same")
    return num1,  num2
  
num1 = int(input("Enter any num1:"))
num2 = int(input("Enter any num2:"))
compare(num1,num2)
"""

#Tehtävä 107-3: Tee ohjelma, johon syötetään 2 nimeä ja ikää. Kerro kumpi henkilö on vanhempi.
"""
def compare(person1_age,person2_age):
  if person1_age > person2_age:
    print(person1_name, "is older.")
  else:
    print(person2_name, "is older.")
  return person1_age,person2_age
  
person1_name= input("Enter your name:")
person1_age = int(input("Enter any num1:"))
person2_name= input("Enter your name:")
person2_age = int(input("Enter any num2:"))

compare(person1_age, person2_age)

"""

#Tehtävä 107-4: Tee, ohjelma, johon syötetään kaksi merkkijonoa. Kerro kumpi on ensimmäinen ja viimeinen.

def compare_strings(string1, string2):
    if string1 < string2:
        return string1, string2
    else:
        return string2, string1


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

first, last = compare_strings(string1, string2)
print("First string:", first)
print("Last string:", last)


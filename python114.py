#Python 114


"""funktion määrittely:

def funktionnimi():
		print("Funktio!")

# funktiokutsu

funktionnimi()


#funktiolla voi olla parametrejä

def funktionnimi(etunimi,sukunimi):
		print(f"{etunimi} {sukunimi}")


funktionnimi("Aku","Ankka")

# muuttujan käyttöä funktion sisällä

muuttuja = 111

def funktionnimi():
	print(muuttuja)
	muuttuja += 111

funktionnimi()
print(muuttuja)

muuttuja = 111

def funktionnimi(muuttuja):
	print(muuttuja)
	muuttuja += 111

funktionnimi(123456) # globaali muuttuja ajaa yli
print(muuttuja)

"""

#Tehtävä 114-1: Tee ohjelma, jossa on funktio, joka tulostaa syötetyn parametri.
#Tulosta Akun veljenpojat.
"""
def print_name (name):
  print ("Aku´s nephews name is", name)
  
name = input("Enter mame:") 
print_name(name)
"""

#Tehtävä 114-2: Tee ohjelma, jossa on funktio, joka tulostaa syötetyn parametrin ensimmäisen merkin.
"""
def my_string(string):
  first_character = string[0]
  print(first_character)
  
string = input("Enter any word:")
my_string(string)

"""

#Tehtävä 114-3: Tee ohjelma, jossa on funktio, joka tulostaa syötetyn numeron potenssiin kolme.
"""
def power_of_three (number):
  return number**3

number = float(input("Enter any number:"))
print(power_of_three(number))


def power_of_two (number):
  return number**2

number = float(input("Enter any number:"))
print(power_of_two(number))


#Tee myös funktio, joka tulostaa syötetyn numeron potenssiin kaksi.

def average( num,num1,num2):
  return (num+num1+num2)/3

print(average(3,6,9))
"""

#Tehtävä 114-4: Tee ohjelma, jossa on funktio, joka tulostaa kolmen syötetyn parametrin keskiarvon.

def average( num,num1,num2):
  return (num+num1+num2)/3

print(average(3,6,9))


#Tehtävä 114-5: Tee ohjelma, jossa on funktio, joka ottaa merkkijonon ja luvun ja tulostaa merkkijonon luku monta kertaa.
"""

def my_string( string, number):
    for _ in range(number):
        print(string)


number = int(input("Enter number:"))
string = input("Enter string:")
print(my_string(string, number))
"""
def word(string, number):
  print(string*number)

string = "Hello"
number = 4
print(word(string,4))  

#Tehtävä 114-6: Tee ohjelma, jossa on funktio, joka ottaa kaksi lukua ja piirtää XxY alueen "o" merkillä.


def draw_square(char,x,y):
    counter = 0
    while counter < y:
        print(char*x)
        counter += 1

draw_square('o',3,3)



#Tehtävä 114-7: Tee ohjelma, jossa on funktio, joka ottaa kaksi lukua ja piirtää XxY alueen aluksi "1" ja sitten "0" merkeillä shakkilautana.

def draw_chessboard(x,y):
  numA = 1
  numB = 1
  while numA <= y:
      row = ""
      while numB <= x + numA:
        if numB %2 == 0:
          row = row + "1"
        else:
          row = row + "0"
        numB += 1
      print(row)  
      numA +=1
      numB = numA
draw_chessboard(10,5)        


#Tehtävä 114-5: Tee ohjelma, jossa on funktio, joka ottaa merkkijonon ja piirtää siitä sananeliön

def draw_word_square(word):
    length = len(word)
    if length == 0:
        print("Empty string! Cannot create a word square.")
        return
    
   
    size = int(length ** 0.5)
    if size ** 2 < length:
        size += 1
    
    
    padded_word = word + ' ' * (size ** 2 - length)
    
    # Draw the word square
    for i in range(size):
        for j in range(size):
            print(padded_word[i*size + j], end=' ')
        print()


input_word = input("Enter a word: ")
draw_word_square(input_word)



def draw_WordSquare(word):
   counter1 = 0
   row = word * 2
   while counter1 < len(word):
     print(row[counter1:len(word)+counter1])
     counter1 += 1
word = "Hello"
draw_WordSquare(word)     
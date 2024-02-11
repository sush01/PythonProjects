#Python 115
"""

funktiolla voi olla paluuarvo ja sen suositeltu tietotyyppi voidaan määrittää:

def funktionnimi(muuttuja):
	return muuttuja += 1234

def funktionnimi(muuttuja:int):
	return muuttuja += 1234

def funktionnimi(muuttuja:int) -> int:
	return muuttuja += 1234
 
"""

#Seuraavaksi kutsutaan funktioita toisista funktioista.

#Tehtävä 115-1: Tee ohjelma, jonka funktio palauttaa anntuista parametreista pienimmän
"""
def print_smallest(num,num1,num2):
  if num < num1 and num < num2:
    print(num,"is smallest among", num,"," ,num1,",", num2)
  elif num1 < num2 :
    print(num1, "is smallest among", num,",", num1,",",num2)
  else:
    print(num2, "is smallest among", num,",",num1,",",num2) 
    
print_smallest(2,4,6)    
print_smallest(9,5,1)
"""

num = 12.09
num1 = 13.98

def print_smallest( num, num1):
  if num <= num1:
    result = num
  else: 
    result = num1
  return result
print(print_smallest(num,num1))


#Tehtävä 115-2: Tee ohjelma, jonka funktio ilmoittaa onko annettu merkki sama tai ei (True tai false)
"""
def check_character(char,char1 ):
  return char == char1
print(check_character("k","K"))
print(check_character("0","0"))
print(check_character("a","a"))
"""
word1 = "Kukka"
word2 = "Lukka"

def compare( word1, word2):
  return word1 == word2

print(compare(word1,word2))


#Tehtävä 115-3: Tee ohjelma, jossa
#on funktio, joka piirtää parametrina annettua merkkiä annetun luvun verran.
#Tee funktio joka piirtää näin neliön annettua merkkiä.
"""
def draw_character( char, width, height):
  for _ in range (height):
   print(char * width)
  
draw_character( "#", 8,3)  
"""
"""
def draw_character( char, width, height):
  for _ in range (height):
   print(char * width)
  
draw_character( "#",8,3) 
"""  


def make_row(char, number):
  print(char*number)
  
def drawsquare(char,number):
  count = 0
  while count < number:
    make_row(char, number)  
    count+=1
drawsquare("*",5)    
    
#Tehtävä 115-4: Tee ohjelma, jossa
#on funktio, joka piirtää parametrina annettua merkkiä annetun luvun verran.
#Tee funktio joka piirtää näin nelikulmion annettua merkkiä.

def makerow(char, number):
  print(char*number)
  
def drawsquare(char,x,y):
  count = 0
  while count < y:
    make_row(char, x)  
    count+=1
drawsquare("#",5,2)    

"""
def draw_character( char, width, height):
  for _ in range (height):
   print(char * width)
  
draw_character( "#",8,3) 
""" 
#Tehtävä 115-5: Tee ohjelma, joka piirtää funktiossa joulukuusen "*" merkeillä.
#Tee toinen funktio, joka antaa sille parametrit


def draw_tree( height):
  for i in range (1,height+1):
   print(" " * (height-i) + "*" * (2 * i - 1))
   
   trunk = 2
  for _ in range (trunk):
    print(" " * (height-trunk) + "*" * trunk) 
   
draw_tree(5)  



def drw_christmas_tree(height):
  counter = 0
  while( counter <= height):
    tree = " "*(height-counter)+ "*" * (2*counter+1)
    print(tree)
    counter += 1
def draw_tree():
  height= int(input("Enter Chrismas tree´s height:"))
  drw_christmas_tree(height)
  
draw_tree()     


#Tehtävä 115-6: Tee ohjelma, joka piirtää funktioilla nelikulmioita ja joulukuusia.
#Tee toinen funktio, joka antaa sille parametrit ja piirrä erilaisia muotoja.

def piirrajotain():
  draw_tree()
  drawsquare("*",5,4)
  draw_tree ()

piirrajotain()

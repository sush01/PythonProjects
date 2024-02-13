#Python 111

"""
Yhdistä merkkijonot + merkillä
print("aarne" + "bertta")

kerro merkkijonot * merkillä 
print("Aku"*3)


Tulosta merkkijonon eka merkki
järjestys alkaa kohdasta 0 ja jatkaa siitä
muuttuja = "saippuakauppias"
print(muuttuja[0])

print(muuttuja[0:3])
print(muuttuja[4:10])

# jos alkukohta puuttuu, se on oletuksena 0
print(muuttuja[:3])

# jos loppukohta puuttuu, se on oletuksena merkkijonon pituus
print(muuttuja[4:])

muuttuja.find("a")


#Tehtävä 111-1: Piirrä joulukuusi * merkeillä. Syötä ensin joulukuusen korkeus numerona.
height = int(input("Enter height of the Christmas tree:"))
counter = 0
while (counter <= height):
  tree = " " * (height-counter)+ "*" * (counter*2 +1)
  print(tree)
  counter += 1  
  
 """
#Tehtävä 111-2: Syötä merkkijono ja toistojen lukumäärä. Tulosta sitten merkkijono toistettuna.

my_string = input("Enter word:")
num_repeat = int(input("Enter number of times it should repeat:"))
print(f"{my_string} is repeated {num_repeat}timees: {my_string*num_repeat}" )


#Tehtävä 111-3: Syötä merkkijono ja tulosta se. Lisää vielä "=" merkeillä merkkijonon pituinen alleviivaus.
my_string = input("Enter word:")
print(f"{my_string} {len(my_string)* '='}")



#Tehtävä 111-4: Syötä kaksi merkkijonoa ja kerro kumpi on pitempi
my_string1 = input("Enter first word:")
my_string2 = input("Enter second word:")
if len(my_string1)> len(my_string2):
  print(f"{my_string1} is longer than {my_string2}")
  
elif len(my_string1)< len(my_string2):
  print(f"{my_string2} is longer than {my_string1}")
else:
  print(f"{my_string1} and {my_string2} are both same length")
  


#Tehtävä 111-5: Syötä merkkijono ja tulosta sen merkit viimeisestä ensimmäiseen

my_string = input("Enter word:")
counter = len(my_string)
while (counter > 0): 
  print(my_string[counter-1])
  counter -= 1


#Tehtävä 111-6: Syötä merkkijono ja tulosta sen toinen ja toiseksi viimeinen merkki
my_string = input("Enter word:")
print(f" letter in second index is {my_string[1]} and second last letter is {my_string[-2]}")


#Tehtävä 111-7: Syötä merkkijono ja tee siitä uusi merkkijono, jonka merkit ovat päinvastoin

my_string = input("Enter word:")
counter = len(my_string)
result = ""
while ( counter > 0):
  result = result + my_string[counter-1]
  counter -= 1
print(result)    


#Tehtävä 111-8: Syötä merkkijono ja tulosta se niin, että kullakin rivillä on yhdestä pituuteen verran kirjaimia

my_string = input("Enter word: ")
counter = 0
while (counter <= len(my_string)):
    print(f"{my_string[:counter]}")
    counter += 1
    

#Tehtävä 111-9: Tee 20 merkkinen merkkijono "=" merkeistä. Syötä merkkijono, jono korvaa = merkkejä. 
#Tämä merkkijono on lisäksi tasattu oikealle, vasemmalle tai keskelle valinnan mukaan.

my_string = input("Enter word: ")
alignment = 2

if alignment == 0:
    result = my_string + (20-len(my_string))*"="
elif alignment == 1:
    result = (20-len(my_string))*"=" + my_string
else:
  result = (10-int(len(my_string)/2))*"=" + my_string + (10-int(len(my_string)/2))*"="    
print(result)



#Trehtävä 111-10: Syötä merkkijono ja etsi kaikki vokaalit

my_string = input("Enter word: ")
result = ""
vowels = "aeiouyäöAEIOUYÄÖ"

for char in my_string:
    if char in vowels:
        result += char

print(result)


my_string = input("Enter word: ")
counter = 0
result = ""
while counter < len(my_string):
  counter1 = 0
  vowel =  "aeiouyäöAEIOUYÄÖ"
  while counter1 < len(vowel):
    if my_string[counter].find(vowel[counter1]) != -1:
        result = result + my_string[counter]
    counter1 += 1
  counter += 1
print(result)      






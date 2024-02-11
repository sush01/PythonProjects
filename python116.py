#python 116

"""
listat

lista = []
lista = [11,22,33]

print(lista[0])
print(len(lista[0]))

Lisää listaan
lista.append(123) # loppuun

lista.insert(0,111) # (X,Y) X indeksiin Y arvo

Poista listasta
lista.pop(1) # poistaa indeksistä

if 1 in lista:
	lista.remove(1) # poistaa arvon

lista.sort()

uusilista = sorted(lista)

max ja min funktioilla voit ottaa listan suurimman ja pienimmän arvon
"""

#Tehtävä 116-1: Tee ohjelma, johon kuuluu lista = [0,0,0,0,0,0,0,0,0,0] syötetään indeksi 0+ ja luku arvoksi. Täytä listaa ja tulosta joka syötön jälkeen listan sisältö.
"""
list = [0,0,0,0,0,0,0,0,0,0]
while True:
  index = int(input("Enter index (0-9):"))
  arvo = int(input("Enter value to insert at index:"))
  if index == -1:
    break
  list[index] = arvo
  print(list)
"""
#Tehtävä 116-2: Tee ohjelma, johon syötetään X kappaletta numeroita. Tulosta luotu lista lopuksi.
"""
list = []
count = 0
while count < 6:
    value = int(input("Enter value:"))
    list.append(value)
    count += 1
print(list)  

"""



#Tehtävä 116-3: Tee ohjelma, jossa on lista, johon voi lisätä ja poistaa arvoja.
"""
list = []
while True:
  choice = int(input("Options to add = 1, end = 0 ,delete = -1:"))
  value = int(input("Enter value:"))
  if choice == 1:
    list.append(value)
  elif choice == 0:
    break
  else:
    if value in list:
      list.remove(value)
  print(list)    

"""
#Tehtävä 116-4: Tee ohjelma, johon syötetään sanoja. Pysäytä se, jos sama sana tuli kahdesti.
"""
list = []
while True:
  word = input("Enter any word:")
  if word in list:
    print("Word already exists in the list!")
    break
  list.append(word)
  print(word)
  print(list)
"""

#Tehtävä 116-5: Tee ohjelma, johon syötetään numeroita. Tulosta joka numeron jälkeen lista sekä sen järjestetty versio.
"""
list = []
while True:
  number = int(input("Enter number:"))
  list.append(number)
  print(f"List of numbers {list}")
  print(f"Sorted list is {sorted(list)}")
"""
#Tehtävä 116-6: Tee ohjelma, johon syötetään numeroita. Tulosta joka numeron jälkeen suurin ja pienin arvo.
"""
list = []
while True:
  number = int(input("Enter number:"))
  if number == -1:
    break
  list.append(number)  
  print("List is",list)
  print("Largest number is:", max(list))
  print("Smallest number is:",min(list))
"""



#Tehtävä 116-7: Tee ohjelma, jossa on funktio, joka ottaa listan parametrina. Järjestä lista ja anna se paluuarvona
def sorted_list(list):
    return sorted(list)

list = [22,33,54,11,34,87,99]
print(sorted_list(list))  



#Tehtävä 116-8: Tee ohjelma, jossa on funktio, joka ottaa listan parametrina. palauta listan pituus paluuarvona.
def length(list):
   return len(list)

list = [11,44,77,98,99,23,12]
print(length(list))
#Tehtävä 116-9: Tee ohjelma, jossa on funktio, joka ottaa listan parametrina. palauta listan keskiarvo paluuarvona.

def calculate_average(list):
    return sum(list)/len(list)
  
list = [11,44,77,98,99,23,12]
print(calculate_average(list))
  



#Tehtävä 116-10: Tee ohjelma, jossa on funktio, joka ottaa listan parametrina. 
# palauta listan vaihteluväli (suurin miinus pienin arvo) paluuarvona.


def check_list(list):
  return max(list)-min (list)

list = [1,4,7,8,9,3,12]
print(check_list(list))

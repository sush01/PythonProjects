#Python 121


# dictionary

muuttuja = {}

muuttuja["123"] = "Aku"
muuttuja["456"] = "Iines"
muuttuja["999"] = "Roope"

print(muuttuja)
print(muuttuja["123"])


muuttuja["A"] = "Jukka"
muuttuja["A"] = "Pekka"
muuttuja["A"] = "Pekka"
muuttuja["A"] = "Pekka"
print(muuttuja)


for avain, arvo in muuttuja.items():
	print(f"{avain} ja {arvo}")
del muuttuja["999"]


#Tehtävä 121-1: Tee funktio, jolle syötetään luku X ja funktio asettaa sille arvoksi X*123

def insert_number(x:int):
  number[x] = x*123

number = {}
insert_number(6)
print(number)

#Tehtävä 121-2: Tee funktio, jolle syötetään merkkijonoja. Funktio ei salli duplikaatteja.

def insert_word(word:str):
   word1[word]= word
   
word1 = {}
insert_word("Tupu")
insert_word("Kuku")
insert_word("Luku")
print(word1)   



#Tehtävä 121-3: Tee funktio, jolle syötetään merkkijono. Se ottaa talteen merkkijonon kirjaimet ja tulostaa "*" merkkejä yhtä monta kertaa kuin kirjain löytyy merkkijonosta.

def insertWord(word:str):
  for letter in word:
    word2[letter]= ""
  for letter in word:
    word2[letter] += "*"
      
word2 = {}
insertWord("Christmastree")
print(word2)


#Tehtävä 121-4: Tee ohjelma, johon syötetään puhelinnumeroita ja henkilöitä. Tulosta lopuksi kaikki tiedot.
"""
def insert_phoneno(name:str, num:int):
  person_info[name]= num
  

person_info = {}  
insert_phoneno("Sushila", 234567)
insert_phoneno("John", 9876543)
print(person_info)

for key, value in person_info.items():
  print(f"{key} phone number is {value}")
"""



#Tehtävä 121-5: Tee ohjelma, johon syötetään ja poistetaan puhelinnumeroita ja henkilöitä. Tulosta lopuksi kaikki tiedot.
"""
def insert_phoneno(name:str, num:int):
  person_info[name]= num
  
def delete_phoneno(name:str):
  del person_info[name]

person_info = {} 
while True:
  choice = int(input(" Enter -1 = end, 0 = delete, 1 = add:"))

  if choice == -1:
    break
  elif choice == 1:
    name = input("Enter name:")
    num = int(input("Enter phone number:"))
    insert_phoneno(name,num)
  elif choice ==0:
    name = input("Enter name to delete:")
    delete_phoneno(name)
  else:
    print("Invalid Choice")
print(person_info)  

"""
#Tehtävä 121-6: Tee ohjelma, jolle syötetään dictionary. Muuta avaimet arvoiksi ja päinvastoin.

def change_value(my_dict:dict):
  dummy = {}
  for key, value in my_dict.items():
    dummy[value]= key
  return dummy  

my_dict = { "1": "Luku", "2": "Duku"}
print(my_dict)
my_dict = change_value(my_dict)
print(my_dict)

#Tehtävä 121-7: Tee ohjelma, johon syötetään kirjan nimi ja tekijä sekä vuosi niin, että kukin kirja on yksi dictionary.
#Tee lista dictionaryista ja tulosta niiden sisältö.
lista = []

while True:
    book_name = input("Enter book name: ")
    if book_name== "":
        break
    author = input("Enter author name:")
    year = int(input("Enter year: "))
    dummy = {"Book": book_name, "Author": author, "Year": year}
    lista.append(dummy)

for info in lista:
    print(info)

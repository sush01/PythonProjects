#Python 123
import csv

"""
with open("testi.txt") as tiedosto:
    teksti = tiedosto.read()
    print(teksti)
	
lista =[]
with open("testi.txt") as tiedosto:
    for rivi in tiedosto:
		lista.append(rivi)
		print(rivi)

lista =[]
with open("testi.txt") as tiedosto:
    for rivi in tiedosto:
		sanalista = rivi.split(";")
		lista.append(sanalista)
		for sana in sanalista:
			print(sana)
"""	
# \n pääsee eroon .strip() lauseella voit kokeilla myös .replace lausetta

#Tehtävä 123-1: Tee tiedosto, jossa on monta riviä numeroita. Lue se ja tulosta numerot.
#Make a file with many line of numbers.Read it and print the numbers

"""
list =[]
with open("number.txt") as file:
    for row in file:
      list.append(int(row))
      print(row)
print(list)        
"""
#Tehtävä 123-2: Tee .csv tiedosto, jossa on monta riviä ";" erotettuja sanoja. Lue se ja luo lista sanoista.
# Make a .csv file with many lines ";" seperated words.Read it and make a list of words

list = []
filename = "testi.csv"
"""
with open(filename, "w", newline="") as file:
  
  writer = csv.writer(file)
  
  writer.writerows(list)
  
print(f"CSV file '{filename}' has been created successfully.")
"""
"""
with open("text.csv")as file:
    for row in file:
      wordlist = row.split(";")
      list1 = []
      for word in wordlist:
        list1.append(word.strip())
        list.append(list1)
print(list)        
"""          
#Tehtävä 123-3: Tee .csv tiedosto, jossa on monta riviä ";" erotettuja sanoja sekä välilyöntejä. Lue se ja luo lista sanoista. Poista rivinvaihdot ja turhat välilyönnit.
#Make a .cvs file with many lines ";" seperated words and spaces.  Read it and make a lists of words.Remove line breaks and unneccessary spaces.
"""
lista =[]
filename = "testi.csv"
with open("testi.csv") as file:
    for row in file:
        sanalista = row.split(";")
        dummy = []
        for sana in sanalista:
            dummy.append(sana.strip())
        lista.append(dummy)
print(lista)	
"""
#Tehtävä 123-4: Yhdistä kahden .csv tiedoston sisällöt ja tee niistä listan arvoja.
#Combine the contents of two .cvs files and make them into a list of values.

list = []
with open ("testi.csv") as file:
  for row in file:
    wordlist = row.split(";")
    list1 = []
    for word in wordlist:
      list1.append(word.strip())
      list.append(list1)

with open ("text.csv") as file:
  for row in file:
    wordlist = row.split(";")
    list1 = []
    for word in wordlist:
      list1.append(word.strip())
      list.append(list1)
print(list)      

import csv


"""
with open("testi.txt", "w") as tiedosto:
    tiedosto.write("Tupu\n")
    tiedosto.write("Tupu\n")
    tiedosto.write("Tupu\n")

# tyhjää tiedosto
open("testi.txt", "w").close()
"""
#tuhoa tiedosto

#import os 

#os.remove("testi.txt")

#Tehtävä 124-1: Tee ohjelma, jolle syötetään lauseita, jotka kirjoitetaan lopuksi tiedostoon.

fileobject = open("testi.txt","w+")

fileobject.write("Tupu\n")
fileobject.write("Hupu\n")
fileobject.write("Tupu\n")

fileobject = open("testi.txt","r")
result = fileobject.readlines()
print(result)


#Tehtävä 124-2: Tee ohjelma, jolle syötetään nimi ja ikä pareja. Ohjelma kirjoittaa sen .csv tiedostoksi.
#Erota tiedot ";" merkillä.


with open("testi.txt")as mycsvfile:
  inputstream = csv.reader(mycsvfile, delimiter =";")
  title = True
  for row in inputstream:
    if title:
      print(row)
      title = False
    else:
      print("{} {}".format(row[0], row[2])) 

#Tehtävä 124-3: Tee ohjelma, jolle voidaan syöttää lauseita tai lukea mitä on kirjoitettu. 
#Käytä numerointia erottamaan lauseet.



#Python 110

"""
luupissa voi olla myös ehto

# alustus
luku = int(input("Anna luku: "))

# tulosta
while luku < 10:
    print(luku)
#muutos luupin kierroksien välillä
    luku += 1
"""
#Tehtävä 110-1: Tulosta joka kolmas luku välillä 1 ja 50.
number = 1
while number <= 50:
    print(number)
    number += 3


#Tehtävä 110-2: Tee uusiksi lähtölaskentatehtävä niin että siinä ei ole while True: riviä 
#vaan jotain muunlainen rivi.

number = 7
while number > 0:
    print(number)
    number -= 1


#Tehtävä 110-3: Tulosta luvut 1stä eteenpäin käyttäjän antamaan lukuun asti.

number = int(input("Enter number:"))
count = 1
while count < number:
    print(count)
    count += 1


#Tehtävä 110-4: Tulosta aluksi 1 ja sitten seuraava luku niin että se on edellisen luvun arvo kerrottuna kahdella.

counter = 1
while counter < 100:
    print(counter)
    counter *= 2

#Tehtävä 110-5: kysy kaksi lukua ja tulosta sen potenssit arvosta 0 toiseen lukuun asti

number1 = int(input("Enter number:"))
number2 = int(input("Enter number:"))
counter = 0
while counter <= number2:
    print(f"{number1} potenssi {counter} on {number1**counter}")
    counter += 1



#Tehtävä 110-6: Kysy käyttäjältä luku ja tee ohjelma joka laskee 1+2+3... kunnes summa on käyttäjältä saatu luku tai sitä pienempi edellinen luku. Näytä tiedot "1+2+3..." tavalla.

number = int(input("Enter number:"))
counter = 0
sum = 0
text = ""
while sum <= number:
    sum += counter
    if (counter == 0):
        text = str(counter)
    else:
        text = text + f"+{counter}"
    print(f"{counter}: {text} = {sum}")
    counter += 1
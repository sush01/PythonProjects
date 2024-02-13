#Python 109
# ikiluuppi
"""
while True:
    luku = int(input("Anna luku? "))
    if luku == -1:
        break
    print(luku)

# nouseva luku
iteraattori = 0
while True:
	print(iteraattori)
	iteraattori = iteraattori + 1
	if iteraattori > 5:
		break;
"""

# Tehtävä 109-1: Tee toistolause, joka jatkuu kunnes käyttäjä kirjoittaa "ei"
while True:
    answer = input("Write something:")
    if answer == "no":
        break
    print(answer)

# Tehtävä 109-2: Tee toistolause, joka jatkuu kunnes käyttäjä kirjoittaa luvun välillä 1 ja 100

continuesloop = True
while continuesloop:
    number = int(input("Enter number or (enter 0 to quit):"))
    if number == 0:
        print("Bye Bye!")
        continuesloop = False
    elif number < 100 or number < 0:
        print("Enter number is from range 1-100.")
    else:
        print("Number is :", number)
        


# Tehtävä 109-3: Syötä salasana. Tee toistolause, joka jatkuu kunnes käyttäjä kirjoittaa <salasana>.

password = input("Enter your password:")
while True:
    ans = input("Enter your password:")
    if ans == password:
        break
    print("Successfully logged in!")



# Tehtävä 109-3: Syötä salanumero. Tee toistolause, joka jatkuu kunnes käyttäjä kirjoittaa <salanumero>.
#Pysäytä tehtävä, jos yrityksiä on enemmän kuin kolme.

pass_code = int(input("Enter your passcode:"))
result = 0
while True:
    answer = int(input("Enter your passcode:"))
    result += 1
    if answer == pass_code:
        print("You are identified!")
        break
    elif result >= 3:
        print("Too many attempts!")
        break


# Tehtävä 109-4: Tee lähtölaskenta arvosta 8 arvoon 1, jonka jälkeen kirjoita "Laukaisu!"

count = 8
while True:
    print(count)
    count -=1
    if count == 0:
        break 
    print("Laukaisu!")




# Tehtävä 109-5: Tee toistolause, johon syötetään lukuja kunnes käyttäjä kirjoittaa -1. Laske tämän jälkeen keskiarvo.


count = 0
sum = 0

while True:
    num = int(input("Enter number:"))
    if num == -1:
        break
    sum += num
    count +=1
    print(f"Average is {sum/count}")





#Python 105

#Tavoitteet:
#-Ymmärtää if-lauseita

"""if ika > 17:
    print("Tässä ajokortti!")
else:
	print("Polkupyörä on keksitty!")"""
 

#Tehtävä 105-1: Tee ohjelma, joka kysyy vuoden ja sanoo syntymävuotesi, jos kyseessä on vuosi jolloin synnyit.
"""print("Enter any year:")
year = int(input())
if year == 1991:
    print("This is your birth year!")
else:
    print("Not your birth year try again!")
"""
#Tehtävä 105-2: Tee ohjelma, joka antaa luvun itseisarvon. Sen on katsottava onko luku pienmpi kuin 0 ja tällöin kertoo luvun -1:llä.
"""
def absolute_value(number):
    if number < 0:
        return number * -1
    else:
        return number
    
number = float(input("Enter a number:"))
print("Absolute value of ", number, "is", absolute_value(number))



number = -20
absolute_number = abs(number)
print(absolute_number)

"""



#Tehtävä 105-3: Tee ohjelma, joka kysyy nimen ja lukumäärän. Nimen ollessa Aapeli, ohjelma sanoo että tässä ilmainen ruoka. Muuten ohjelma sanoo, että annokset maksavat lukumäärä kertaa 5,90 euroa.
"""
def check_cost(name, number):
    if name.lower() == "aapeli":
        print("Here is free food for your", name)
        
    else: 
        cost = 5.90 * number
        print("Hello", name + ",", "the cost for", number,"portions cost","{:.2f}".format(cost), "euros")
        

name = input("Enter your name:")
number = int(input("Enter number of portion:"))

check_cost(name,number)
"""
#Tehtävä 105-3: Ohjelmalle syötetään luku. Se ilmoittaa että luku on pienempi kuin 10/100/1000/10000
"""
def check_number(number):
    if number < 10:
        print("Entered number is less than 10.")
    elif number < 100:
        print("Entered number is less than 100.")
    elif number < 1000:
        print("Entered number is less than 1000.")
    elif number < 10000:
        print("Entered number is less than 10000.")
    else:
        print("Number is equal to or greater than 10000.")
    
number = int(input("Enter number:"))   
check_number(number) 
"""
#Tehtävä 105-4: Ohjelmalle syötetään kaksi lukua ja laskentatapa (plus, miinus, kerto, jako). 
#Ohjelma laskee laskentatavan mukaisen tuloksen ja tulostaa sen.

#Tehtävä 105-5: Tee ohjelma, jolle syötetään luku Celsiusasteina. Ohjelma ilmoittaa arvon Fahrenheitteina. Etsi kaava netistä.
celsius = float(input("Enter number in celsius:"))

fahrenheit = (celsius * 1.8) + 32

print(  " Celsius is equivalent to Fahrenheit is:" ,fahrenheit)
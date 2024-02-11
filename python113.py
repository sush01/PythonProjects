# Python 113
# ==========

# break - hyppää ulos silmukasta
# continue - palaa silmukan alkuun
"""
summa = 0
while True:
    luku = int(input("Anna luku "))
    if luku == -1:
        break
    summa += luku
	
summa = 0
luku = 0
while luku != -1:
    luku = int(input("Anna luku "))
    if luku != -1:
        summa += luku

summa = 0
while True:
    luku = int(input("Anna luku "))
    if luku == -1:
        break
    if luku >= 10:
        continue
    summa += luku
"""

# Monien silmukoiden tapauksessa break hyppää aina seuraavaan ulommaiseen silmukkaan

# Tehtävä 113-1: Tee ohjelma, joka laskee kertotaulun lukuun X asti, eli (esim 2) 1x1, 1xX, Xx1, XxX...
"""
number = int(input("Enter number: "))
counter = 1
counter1 = 1
while counter <= number:
    while counter1 <= number:
        print(f"{counter} * {counter1} = {counter*counter1}")
        counter += 1
    counter1 = 1
    counter += 1
"""

# Tehtävä 113-2: Tee ohjelma, jolle syötät lauseen. Tulosta jokaisen sanan ensimmäinen kirjain.
"""
word = input("Enter any word:")
count = 0
while count < len(word):
    if count ==0:
        print(word[count])
    if (" "in word[count]):
        print(word[count+1])
    count += 1  
      
"""

# Tehtävä 113-3: Tee ohjelma, joka laskee annetun luvun X kertoman (esim 4) 1*2*3*X = ...
"""
x = int(input("Enter number:"))
count = 1
result = 1
text = ""
while count <= x:
  text = text + str(count)+ "*"
  result *= count
  print(f"{count} gets value {text[:-1]} = {result} ")
  count += 1
  
  
############
def calculate_product(x):
    product = 1
    i = 1
    while i <= x:
      product *= i
      i += 1
    return product 
  
x = int(input("Enter a number (x):"))
result = calculate_product(x)
 
##############  
x = int(input("Enter number: "))
count = 1
result = 1
text = ""

while count <= x:
    text = text + str(count) + "*"
    result *= count
    count += 1

print(f"{text[:-1]} = {result}")
  
"""

# Tehtävä 113-4: Tee ohjelma, joka tulostaa kaikki luvut käyttäjän antamaan lukuun asti.
# Tee ohjelma niin, että kukin pari lukuja esitetään suurempi ensin.

    
y = int(input("Enter number: "))
count = 1
result = 1
text = ""

while count <= y:
  if count % 2 != 0 and count == y:
    text = text + str(count) 
    print(f"{text}")
    break
  else:
    text = text + str(count+1) + " " + str(count) + " "
    count += 2
  print(text)



# Tehtävä 113-5: Tee ohjelma, joka tulostaa kaikki luvut käyttäjän antamaan lukuun asti.
# Tee ohjelma niin, että ensin esitetään 1, sitten X, sitten 2, sitten X-1 jne...

z = int(input("Enter number: "))
count = 1
result = 1
text = ""

while count <= z:
    text = text + str(count) + " " + str(z - count + 1) + " "
    print(f"{text}")
    if count == z - count + 1 or count == z - count:
      break
    count += 1
    
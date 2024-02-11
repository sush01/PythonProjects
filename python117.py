#python 117

"""
listat

lista = [12,44,66,44]

for elementti in lista:
    print(elementti)

for elementti in range(5):
    print(elementti)

range(2, 5)
range(2, 10, 2)

lista = list(range(5))
"""

#Tehtävä 117-1: Tulosta merkkijono niin että kukin kirjain tulee omalle rivilleen ja kirjainten väliin tulee "%" merkki.
"""
word = "Summer"
for element in word:
  print(word)
"""

#Tehtävä 117-2: Tulosta luku niin että luku pienenee luvusta -lukuun asti.
"""
number = int(input("Enter number:"))
if number > 0:
  print(list(range(number, -number, -1)) + [-number])
else:
  print(list(range(number,-number,1)) + [-number])  

"""
#Tehtävä 117-3: Tulosta "*" niin, että kullekin riville tulee se lukumäärä, joka on listan elementti.
"""
list = [2,3,4,5,6]
for element in list:
  print("*"*element)
"""
#Tehtävä 117-4: ilmoita onko merkkijono anagrammi (täsmälleen samat kirjaimet) toisen merkkijonon kanssa
"""
word1 = "heart"
word2 = "earth"

if sorted(word1) == sorted(word2):
  print(f"Word {word1} and {word2} are anagrams")
else:
  print(f"Word {word1} and {word2} are not anagrams")
"""

#Tehtävä 117-5: ilmoita onko merkkijono palindromi (täsmälleen sama käännettynä toisinpäin) toisen merkkijonon kanssa



#Tehtävä 117-6: laske yhteen ainoastaan negatiiviset numerot, jotka ovat listassa.
"""
list = [-1,3,6,7,-2]
sum = 0
for element in list:
  if element < 0:
    sum += element
print(sum)    
"""
#Tehtävä 117-7: ilmoita parilliset luvut listasta.

list = [-1,3,6,7,8]
result = []
for element in list:
  if element % 2 == 0:
    result.append(element)
    
print(result)    


#Tehtävä 117-8: Laske yhteen kahden listan elementit.
"""
list1 = [-1,3,6,7]
list2 = [-1,3,6,-2]

calculate = 0
list = []
for element in list1:
  list.append(element+list2[calculate])
  calculate += 1
print(list)  
"""

#Tehtävä 117-9: Hae listasta ne elementit, joille ei ole paria.
#Find the elements that have pair 
"""
list = [9,6,3,6,1,2,4,9,3]
result = []

count = {}
for element in list:
  count[element]= count.get(element,0)+1
  
for element, counter in count.items():
  if counter > 1:
      result.append(element)
    
print(result)    
"""


#Tehtävä 117-10: Ilmoita lyhin listan merkkijono
list = ["Hello","Sush","Kandel"]
result = list[0]
for element in list:
  if len(element) < len(result):
    result = element
print(result)


#Tehtävä 117-11: Ilmoita pisimmän listan merkkijonon pituus ja näytä se

list = ["Hello","Sush","Kandel"]
result = list[0]
for element in list:
  if len(element) > len(result):
    result = element
print(f"Longest word in the list is {result}, Its length is {len(result)}")

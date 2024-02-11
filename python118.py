#Python 118

"""
merkkijono = "testi"
print(f"{merkkijono:5} pälä pälä {merkkijono:5}")

liukuluku = 12345.12345
print(f"{liukuluku:.2f} pälä pälä {liukuluku}")

merkkijono = "saippuakauppias"
print(merkkijono[0:10:2])

merkkijono = "testi"
print(merkkijono[::-1])

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista[5:2:-1])

merkkijono = "saippuakauppias"
merkkijono.count("a")

uusimerkkijono = merkkijono.replace("a","A")
"""

#Tehtävä 118-1: Tee merkkijonoja listassa, esitä elementit väärinpäin ja kukin merkkijono väärinpäin
#Task 118-1: Make strings in a list, present the elements upside down and each string upside down
"""
list1 = ["Apple","Kiwi","Orange" ]
for element in list1[::-1]:
  print(element[::-1])
  
list = "Orange"
print(list[::-1])

"""
#Tehtävä 118-2: Ilmoita mitä kirjainta on eniten merkkijonossa...
"""
word = "Suomalainen"
for letter in "abcdefghijklmnopqrstuvwxyz":
  counter = word.count(letter)
  if counter > 0:
      print(f"Letter {letter} is repeated {counter} times")
"""
#Tehtävä 118-3: Poista merkkijonosta kaikki vokaalit
"""
word1 = "Suomalainen"
for letter in "aieou":
  word1 = word1.replace(letter,"")
print(word1)
 """ 
#Tehtävä 118-4: Ilmoita numerolistan elementtien läheinen arvo (etäisyys 1)


my_list = [2,4,7,2,8,9,6,5]
count = 0

while count < len(my_list):
    if count == 0:
        if abs(my_list[count] - my_list[count + 1]) <= 1:
            print(f"Index {count} value is {my_list[count]}")
    elif count == len(my_list) - 1:
        if abs(my_list[count] - my_list[count - 1]) <= 1:
            print(f"Index {count} value is {my_list[count]}")
    else:
          if abs(my_list[count] - my_list[count + 1]) <= 1 or abs(my_list[count]- my_list[count - 1]) <= 1:
              print(f"Index {count} value is {my_list[count]}")
    count += 1
    

    
    
    
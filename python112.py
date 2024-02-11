#Python112


#Merkkijonoja

# osajono
"""
osajono = "joki"
merkkijono = "Seinäjoki"

print("jo" in merkkkijono) # true
print(osajono in merkkkijono) # true

print(merkkijono.find("jo")) # ilmoittaa indeksin
print(merkkijono.find("xxx")) # ei löydy, palauttaa -1
"""
#Tehtävä 112-1: Etsi toinen "i" sanasta "Seinäjoki"
"""
word = "Seinäjoki"
result = []
for index, char in enumerate(word):
  if char == "i":
    result.append(index)

print("Indexes of 'i' in Seinäjoki:", result)    
"""     
word = "Seinäjoki"
result = -1
if ("i" in word):
    count = 0
    while count < len(word):
        if("i" in word[count]):
          result = count
        count += 1
print(result)      


#Tehtävä 112-2: Etsi ja ilmoita kaikki indeksit "i" sanalle sanasta "saippuakauppias"

my_word = "saippuakauppias"
if ( "i" in my_word):
  count = 0
  while count < len(my_word):
    if ("i" in my_word[count]):
      print(count)
    count += 1  
  

#Tehtävä 112-3: Etsi kaikki kolmemerkkiset osajonot, jotka alkavat kirjaimella "a" sanasta "saippuakauppias"

my_word = "saippuakauppias"
if ( "i" in my_word):
  count = 0
  while count < len(my_word):
    if ("i" in my_word[count]):
      print(my_word[count:count+3])
    count += 1  
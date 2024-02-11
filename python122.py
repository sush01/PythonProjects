#Python 122

# Tuplen muodostus

tuple = (123,456)

print(tuple[0])
print(tuple[1])


#Tehtävä 122-1: Tee funktio, joka ottaa 3 parametria ja luo tuplen, johon kuuluu elementit x, y ja z.

def function_tuple(x:int, y:int, z:int):
  #creates tuple from the integers
    tuple = (x,y,z)
    return tuple

#function call with the inputs
result = function_tuple(11,22,44)
print(result)
result = (88,34,2)
print(result)


#Tehtävä 122-2: Tee lista tupleja, joilla on nimi ja ikä. Hae nuorin ja vanhoin.

def person_tuple(name:str,age:int):
 #creates a tuple containing the person´s name and age 
  value = (name, age)
  return value

#Add person tuples to the list using person_tuple function
person_list = []
person_list.append(person_tuple("Sush",30))
person_list.append(person_tuple("John",32))
person_list.append(person_tuple("Emma",18))
print(person_list)

#find and print the maximun age from the list of person tuples
print("Maxmimun age:",max(person_list, key = lambda x: x[1])[1])

#find and print the minimum age from the list of person tuples
print("Minimum age:",min(person_list, key = lambda x: x[1])[1])


#Tehtävä 122-3: Tee lista tupleja, joilla on nimi ja ikä. Hae kaikki ikää X nuoremmat.
 
def find_younger(age1:int):
  for element in person_list:
    if element[1]< age1:
      print(element)

find_younger(30)     
      
#Tehtävä 122-4: Tee ohjelma, jossa on dictionary, johon kuuluu nimi ja X kappaletta opintosuorituksia. 
#Tee opintosuorituksista tupleja.

#function that initialize empty list as a value of dict
def function_student(name:str):
    student[name]= []
  

#function take the list from the person´s name from dictionary
# appends the credit tiple to that list and updates
def scored_credit(person:str, credit:tuple):
  data = student[person]
  data.append(credit)
  student[person] = data

#empty dictionary to store data 
student = {}

#assign data to stundent dict
function_student("Sush")
function_student("John")
function_student("Emma")

#add credits for ech student
scored_credit("Sush",("Physics", 5))
scored_credit("John",("Maths", 4))
scored_credit("Emma",("Chemistry", 6))

#print student dictionary containing data 
print(student)
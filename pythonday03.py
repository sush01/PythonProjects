# olio-ohjelmointia tähän
"""
class Car:
#    color = "red"
#    def __init__(self):
#        self.color = "green"
 
    def __init__(self,color = "white"):
        self.color = color
 
 
 
#    def __init__(self):
#        self.color = "green"
 
def __init__(self,color = "white"):
        self.color = color
        self.model = "Audi"
 
def onoff(self,status):
        # boolean value if engine is on or off
        if status == True:
            print("\nEngine is on!")
        else:
            print("\nEngine is off!")
 
def describecar(self):
        print("I am a {} {}.".format(self.color,self.model))
 
mycar = Car()
print(mycar)
print(mycar.color)
mycar.onoff(True)
mycar.describecar()
 
mycar2 = Car("black")
mycar2.color = "blue"
print(mycar2)
print(mycar.color)
print(mycar2.color)
"""

class Car:
      model = "Audi"
      def __init__(self,color) :
          self.color = color
          
mycarA = Car("White")
mycarB = Car("Black")
mycarB.color = "Yellow"          

print(mycarA.model, mycarA.color)
print(mycarB.model, mycarB.color)


"""

# instance variable <--- olion tasoinen ominaisuus
# --> color
# class variable <--- luokan tasoinen ominaisuus
# --> model
 
class Car:
    model = "Audi"
    def __init__(self,color):
        self.color = color
 
mycarA = Car("White")
mycarB = Car("Black")
mycarB.color = "Yellow"
 
# muutetaan luokan tasoista tietoa
# muuttuu jokaiselle luokan oliolle
Car.model = "Lada"
 
# muuttamalla luokan tasoinen tieto oliolle
# muuttaa sen ainoastaan oliolle
mycarB.model = "Mersu"
 
print(mycarA.model, mycarA.color)
print(mycarB.model, mycarB.color)
 

"""


def ulkoinenfunktio():
    print("ulkoinenfunktio")
 
class Testi:
    def __init__(self,aaa=111,bbb=222,ccc=333):
        self.aaa = aaa
        self.bbb = bbb
        self.ccc = ccc
        ulkoinenfunktio()
        self.kutsujotain()
 
    def kutsujotain(self):
        print("kutsujotain")


testi = Testi(ccc=999)
print(testi.aaa,testi.bbb,testi.ccc)

class Test: 
    def __init__(self):
        self.argAAA = 1234

mytest = Test() 
print(hasattr(mytest,"argAAA"))       
print(hasattr(mytest,"argBBB"))  

if  hasattr(mytest,"argBBB")== False:
    print("Ei ole")


# Task OOP-01
# Program your own class and objects
# Person class with name, age
# personstats()
# personsays(arg)
# Create 2 persons

class Person:

  def __init__(self, name, age):
      self.name = name
      self.age = age

  def personstats(self):
    return f"Name: {self.name}, Age: {self.age}"
  
  def personsays(arg):
    return  arg
      
Person1 = Person("John", 23)
Person2 = Person("Emma", 32)
 
print(Person1.personstats())
print(Person2.personstats())



# Task OOP-02
# change previous solution as follows:
# add class variable number
# its value is increased by 1 whenever new
# person is added
# print how many persons you have created
# i.e. how many Person objects you have

class Person:
  number = 0
  def __init__(self, name, age):
      self.name = name
      self.age = age
      Person.number += 1
    
        
Person1 = Person("John", 23)
Person2 = Person("Emma", 32)

  
print(Person1.name,Person1.age)
print(Person2.name,Person2.age)
print("Number of person added are:",Person.number)
 
 
 

# Task OOP-03
# create class PersonToo
# without default constructor
# attributes are name and age
# methods are personstats() and personsays(arg)
 
class PersonToo:

  def __init__(self, name, age):
      self.name = name
      self.age = age
      
  def personstats(self):
    #return f"Name: {self.name}, Age: {self.age}"
    print(f"Name: {self.name}, Age: {self.age}")

  def personsays(self, message):
   # return f"{self.name} says: {message}"
   print(message)
        
person = PersonToo("John", 43)
print(person.personstats())
print(person.personsays("Hello, How are you!"))

  

# Task OOP-04
# Use class functions and find out following...
# 1) Value of age in both persons.
# 2) Is qwerty a object variable?
# 3) Delete age of one of the persons.
 
class PersonToo:
    name = ""
    age = 0

    def personstats(self):
    #return f"Name: {self.name}, Age: {self.age}"
      print(self.name)
      print(self.age)

    def personsays(self, message):
      #return f"{self.name} says: {message}"
      print(message)
        
person1 = PersonToo()
person1.name = "John"
person1.age = 12
person2 = PersonToo()
person2.name = "Emmi"
person2.age = 23

print(person1.personstats())
print(person1.personsays("Hello, How are you!"))

print(person2.personstats())
print(person2.personsays("Hello, I am fine. What about you?"))
  
print(getattr(person1,"age"))
print(getattr(person2,"age"))

print(hasattr(person1, "qwery"))

delattr(person1, "age")
print(hasattr(person1, "age"))
print(person1.personstats())

# Task OOP-005
# afternoon's programming task.
# create a class BankAccount for accounts
# with attributes:
#   name (string),
#   saldo (float),
#   id (int)
# with methods:
#   changebalance(float) for X amount withdrawal/accumulation
#   accountinfo() that describes account info
# Then add all account objects to a list named accountlist.
 
# Next create a following bank interface to test out your class and list:
#
# MY BANK
# 1: Add account
# 2: Show account info for one account
# 3: Show account info for all accounts
# 0: Quit banking program
     
     
class BankAccount:
  
  def __init__(self, name, saldo, id):
      self.name = name
      self.saldo = saldo
      self.id = id
       

  def accountInfo(self):
    print(self.name, self.saldo, self.id)
    
  def changeBalance(self, amount, choice):
    if choice == "w":
      self.saldo -= amount
    elif choice == "a":
      self.saldo += amount
      
class CreditAccount(BankAccount):
  
      def __init__(self, name, saldo, id,credit):
        self.name = name
        self.saldo = saldo
        self.id = id
        self.credit = credit
        
        
      def accountInfo(self):
          print(self.name, self.saldo, self.id,self.credit)
    
      def changeBalance(self, amount, choice):
        if choice == "r":
          self.credit -= amount
        elif choice == "l":
         self.credit += amount  
         
         
accountlist = []      
account1 = BankAccount("John", 230.0, 23456)
accountlist.append(account1)

acount2 = CreditAccount("Sush", 234.45, 1234, 15000.00)
accountlist.append(acount2)

print(accountlist)
for element in accountlist:
  element.accountInfo()   

#add acount  
def addAccount():
  temp_name = input("Give accounts name:")
  temp_saldo = float(input("Give accounts saldo:"))
  temp_id = int(input("Give accound id:"))
  temp_account = BankAccount(temp_name, temp_saldo, temp_id) 
  accountlist.append(temp_account)
  
# delete account
def deleteAccount():
  name_search = input("Enter the name of the account you want to delete:\n")
  for element in accountlist:
    if element.name == name_search:
      element.remove(element)
      break  

# show info of the account
def showoneAccount():
  name_search = input("Give the name of the account you want to find:\n")
  for element in accountlist:
    if element.name == name_search:
      element.accountInfo()

#show cash transaction of given account
def cashTransaction():
  name_search = input("Enter account name:\n")
  for element in accountlist:
    if element.name == name_search:
      element.accountInfo()
      temp_action = input("Enter your choice w or a\n")
      temp_change = float(input("Enter change of saldo:"))
      element.changeBalance(temp_change, temp_action)
      
# show credit transaction      
def creditTransaction():
  name_search = input("Enter the account name:")
  for element in accountlist:
    if element.name == name_search:
      element.accountInfo()
      temp_action = input("Enter 'r' to raise credit or 'l' to lower credit:\n")
      temp_change = float(input("Enter change of credit:\n"))
      element.changeBalance(temp_change,temp_action)



def showAllAccounts():
  for element in accountlist:
    element.accountInfo()
    
while True: 
  user_input = int(input("\n 1: Add account\n 2: Delete account\n 3: Show account info for one account\n 4: Show account info for all account\n 5: Cash transactions of account\n 6: Credit transactions of account\n 0: Quit banking program\n"))
    
  if user_input == 1:
    addAccount()
  elif user_input == 2:
    deleteAccount()
  elif user_input == 3:
    showoneAccount()
  elif user_input == 4:
    showAllAccounts()
  elif user_input == 5:
    cashTransaction()
  elif user_input ==6:
    creditTransaction()
  elif user_input == 0:
    break             
        
    
# Task OOP-06:
# Change your bank so it includes code set above (polymorphism)
# It must have CreditAccount class
# Add code that shows all bank accounts and credit accounts






# Task OOP-07:
# Change your bank so it includes code set above
# add at least following functionality to bank:
#   Raise or Lower Credit amount for a customer
#   Destroy account
#   Transfer money from one account to another
#   Change Bank account to credit account
#   Change credit account to bank account
#   add information field to account (text content)
#   Allow writing or removing text to information field
#   for instance, "credit risk"
 
       
      
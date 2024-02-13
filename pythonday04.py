#inheritance 
# Inheritance is used for two basic cases
# child class is a special case of mother class
# child class is aggregate of multiple mothers

#practical cases
# child class is a special case of mother class


class Fish:
    def __init__(self, weight,species):
        self.weight = weight
        self.species = species
    
    def swim(self):
      print("Fish swims...")
      
    def eat(self):
        print("Fish eats plakton")    
        
class Shark(Fish):
  # this function is inherted from mother
  #however, it is overriden by child

      def eat(self):
        print("Shark eats Fish")        
        
      def test(self):
        print("test message") 
        
happyfish = Fish(1, "fish")
happyshark = Shark(10, "shark")        
print(happyfish.species)
print(happyshark.species)

happyfish.swim()
happyshark.swim()

happyfish.eat()
happyshark.eat()
happyshark.test()


class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
 
class Student(Person):
    def __init__(self, indexNr, notes, **kwargs):
        # since Employee comes after Student in the mro, pass its arguments using super
        super().__init__(**kwargs)
        self.indexNr = indexNr
        self.notes = notes
 
class Employee(Person):
    def __init__(self, salary, position, **kwargs):
        super().__init__(**kwargs)
        self.salary = salary
        self.position = position
 
class WorkingStudent(Student, Employee):
    def __init__(self, **kwargs):
        # pass all arguments along the mro
        super().__init__(**kwargs)
 
# keyword arguments (not positional arguments like the case above)
ws = WorkingStudent(name="john", last_name="brown", age=18, indexNr=1, notes=[1,2,3], salary=1000, position='Programmer')
print(ws.salary)

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
 
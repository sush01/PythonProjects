# Tuple, Enum, set, dict, functions
"""
list = [11,22,33,44,55,66,77]
mytupleA = ()
print("my empty tuple is",mytupleA)

mytupleB = (4,7,34,5,5,67,87,12)
for index in range(0,len(mytupleB)):
    if mytupleB[index]== 87:
      print("index is", index)
      
arvo1= mytupleB.index(5,0,len(mytupleB))
print(arvo1)
arvo2= mytupleB.index(5,arvo1+1,len(mytupleB))
print(arvo2)


indeksi = 0
for counter in range(0,mytupleB.count(5)):
    indeksi = mytupleB.index(5,indeksi,len(mytupleB))
    print(indeksi)
    indeksi += 1
    
    #enum
    for indeksi,arvo in enumerate(mytupleB):
    if arvo == 5:
        print(indeksi)
 


mysetA = { "eee","ttt","hhh","yyy"}
mysetA.update(["nnn","ggg"])
print(mysetA)
mysetA.remove("nnn")
#mysetA.difference_update(["nnn","ggg"])
mysetA -={ "ttt","eee"}
print(mysetA)

mydictA = dict({"Name": "Aku", "Age": 616})
mydictA[111] = "Testaus"

class kokeilu:
  arvo:111
koe = kokeilu()
koe.arvo  = 123456

#mydictA[koe]= "kokeilu"
print(type(mydictA))
print(mydictA)


koe.arvo = "fhfhfjjkf"
print(mydictA)

"""
#Funtions

"""
def calculatesquare(arg: int):
  return arg**2

print(calculatesquare(4))
result = calculatesquare(4.34)
print(result)

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def calculatesumtwo(arg1: int, agr2: int= 10):
  return arg1*agr2

print(calculatesumtwo(3))
print(calculatesumtwo(3,6))


#arbitary arguments,*args
#Special function

def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus")


def my_list(*args_list):
  finallist = []
  for arg in args_list:
    finallist.append(arg)
  return finallist
  
result = my_list("aa","bb","cc")
print(result)
"""
#arbitary keyword agruments, **kwargs


####
def func(arg):
  return arg

print(func(111))

result = lambda arg:arg

print(result(222))

result1 = lambda agr1, arg2,arg3: agr1+arg2+arg3
print(result1(33,44,66))

full_name = lambda first, last: print(f"Full name: {first} {last}")
print(full_name("Sushila", "Kandel"))
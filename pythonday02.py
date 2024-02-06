#
#
"""
mynumber = int(input ("\nGive a integer number: "))
if mynumber % 2 == 0:
  print("\nEven number")
else:
  print("\nOdd number")


  
temp = int (input ("\n Give a temperature number: "))
if temp <= 10:
    print("\nIt is cold outside")
elif temp > 10 and temp <= 15:
    print("\nIt is warm outside")
else:
    print("\nIt is hot outside")

#numberlist = [1,4,7,9,3,5]
numberlist = (1,4,7,9,3,5)
resultlist = []

for element in numberlist:
  dummy = element * 2
  if element > 4:
    resultlist.append(dummy)
  print("for result is:",resultlist)

## 
myString = "Sushila"
for element in myString:
    if element == 'k':
      pass
    else:
      print(element, end=" ")
      
#pass
myString = "Sushila"
for element in myString:
    if element != 'k':
      print(element, end=" ")
    else:
      print(element, end=" ")
      
## range 
list = [11,22,33,44,55,66,77,88]
for index in range(0, len(list)):
  print(list[index])
  
for element in list:
 print(element)
  
##filter
def filter(value, element):
  if element > value:
    return element
  
result = []
for element in list:
  dummy = filter(44,element)
  if dummy:
    result.append(dummy)
    #result.append(filter(44, element))
print(result)

##map
def map (value, element):
  return element * value

result = []
for element in list:
  result.append(map(3, element))
print(result)"""

##reduce 
"""
def reduce(value, element):
  result = value
  for element in list:
    result -=element
    return result
list = [11,22,33,44,55,66,77,88]
result = reduce(3, list)
print(result)      
  """
#reduce
list = [11,22,33,44,55,66,77,88]
sum = 0
for element in list:
  sum += element
  print(sum)
print(list)
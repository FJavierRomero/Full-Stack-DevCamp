#M2C4 Python Assignment
print("M2C4 Python Assignment")

#Exercise 1: 
print("Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary:")
from decimal import Decimal 

dog_list = ["crowley", "max", "lucas", "leo", "kira"]
print(dog_list)

nephew_tuple = ("izaro", "mikel")
print(nephew_tuple)

number_float = 5.7
print(number_float)

number_integer = 5
print(number_integer)

number_decimal = Decimal(7.55)
print(number_decimal)

owners_dogs_dictionary = {

  "mara" : "crowley",
  "joseba" : "max",
  "deo" : "lucas",
  "mertxy" : "leo",
  "alberto" : "kira",
  
}
print(owners_dogs_dictionary)

#Exercise 2: 
print("Exercise 2: Round your float up:")

import math
print(math.ceil(number_float))

#Exercise 3: 
print("Exercise 3: Get the square root of your float:")

print(math.sqrt(number_float))

#Exercise 4: 
print("Exercise 4: Select the first element from your dictionary:")

print(owners_dogs_dictionary["mara"])

#Exercise 5: 
print("Exercise 5: Select the second element from your tuple:")

print(nephew_tuple[1])

#Exercise 6: 
print("Exercise 6: Add an element to the end of your list:")

dog_list.extend(["tara"])
print(dog_list)

#Exercise 7: 
print("Exercise 7: Replace the first element in your list:")

dog_list[0]="cain"
print(dog_list)

#Exercise 8: 
print("Exercise 8: Sort your list alphabetically:")

dog_list.sort()
print(dog_list)

#Exercise 9: 
print("Exercise 9: Use reassignment to add an element to your tuple:")

nephew_tuple+=("johndoe",)
print(nephew_tuple)


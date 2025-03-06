#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

new_string = 'Javier Romero'
new_number = 2605
new_list = ['Crowley', 'Lucas', 'Leo', 'Kira']
new_boolean: False

print(new_string)
print(new_number)
print(new_list)


#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 

grab_letter = new_string[:3]
print(grab_letter)


#Exercise 3: Use an index to grab the first element from your list.

grab_element = new_list [0]
print(grab_element)


#Exercise 4: Create a new number variable that adds 10 to your original number. 

number_adds = new_number + 10
print(number_adds)


#Exercise 5: Use an index to get the last element in your list. 

grab_element = new_list [-1]
print(grab_element)


#Exercise 6: Use split to transform the following string into a list:

names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')
print(names_list)


"""Exercise 7: Get the first word from your string using indexes. Use the upper function to 
transform the letters into uppercase. Create a new string that takes the uppercase word and the 
rest of the original string."""

first_word = new_string[:6]
first_word = first_word.upper()
upper_string = first_word + new_string[6:]
print(upper_string)


#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

sentence_number = f"this is my number variable: {new_number}"
print(sentence_number)

#Exercise 9: Print “hello world”.

print('hello world')


"""Extra: cadena que contenga la palabra "Hola". Usando la palabra clave en el método de búsqueda o el índice, 
busque y seleccione "Hola" en su cadena. Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós"."""

string = 'cadena con la palabra Hola'
print(string)
busqueda_palabra = string.find('Hola')
print(busqueda_palabra)
new_string = string.replace('Hola', 'adiós')
print(new_string)
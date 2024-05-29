str_manip = input ("Please enter a sentence :)")
#Calculate and print length of str_manip
print(len(str_manip))
#Finding the last letter in the variable and replacing it with @
last_letter = str_manip[-1]
new_letter = '@'
modified_string = str_manip.replace(last_letter,new_letter)
#Printing the last three characters in variable backwards
print (str_manip[-3,])
#Made up word
three_character = str_manip[0:3]
last_two_characters = str_manip[-2:]
Five_letter_character = three_character + last_two_characters
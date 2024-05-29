# Asking the user to input a number
number_input = int(input("Please enter a number" ))
#This variable will sum up all the numbers the user enters
total = 0 
#This variable will keep count of the numbers entered
count = 0 

while number_input != -1:
    number_input = int(input("Please enter a number" ))
    if number_input == -1:
        break
    total += number_input
    count += 1
    average = total / count
    print (f"the average of the numbers entered is: {average}")


   




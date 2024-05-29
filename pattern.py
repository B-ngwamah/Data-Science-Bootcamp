Start_pattern = input ("Type yes to start the pattern")
#The range is 9 because this is the total number of lines and therefore the number of iterations we need
for i in range(9):
    if i < 5:
        #Increasing stars from 1 to 5
        print('*' * (i+1))
    else:
        #Decreasing stars from 4 to 1
        print('*' * (9-i))

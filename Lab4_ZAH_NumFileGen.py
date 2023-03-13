##################################################
###	Title   - Number file creator
###	Author – Zac Huron
###	Date – 2/12/22
###     Description
###         This script will create a file with 20 random integer values
###	    Details
###         1. Requires the os module
###         2. Requires the random module
##################################################  


import os
import random

# Set the file name
file_name = input("Enter file name: ")

# Change the working directory
file_directory = input("Enter file directory: ")
os.chdir(file_directory)

number = input("Enter a number between 2 and 99: ")
number = int(number)

with open(file_name, "w") as file:
    for i in range(1,number):
        random_raw=random.randrange(0,100)
        random_final=int(random_raw)
        
        # convert to a string for the file write
        num_string=str(random_final)
        print(i)
        if i<number - 1:
            num_string= num_string + ","            
        file.write(num_string)

# Close the file - OS can have issues with files that are not closed
file.close()
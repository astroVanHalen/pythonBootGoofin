##################################################
###	Title   - Number file Math Functions
###	Author – Zac Huron
###	Date – 2/21/22
###     Description
###         This script will read a file of 20 values
###				and return values between 20 and 50
###	    Details
###         1. Requires the os module, csv moduleZAH
##################################################  
import os
import csv

# Set the file name
file_name = input("Enter file name to examine: ")
file_name_out = input('Enter name of new file to create: ')

# Change the working directory
file_directory = input("Enter file directory: ")
os.chdir(file_directory)

# Open the input and output files
with open(file_name, 'r') as input, open(file_name_out + '.csv', 'w') as output:
    # Loop over each line in the input file
    for line in input:
        # Split the line into a list of values
        values = line.strip().split(',')
        
        # Convert each value to an integer and check if it's between 20 and 50
        filtered_values = [int(value) for value in values if 20 < int(value) < 50]
        
        # If there are any filtered values, write them to the output file
        if filtered_values:
            output.write(','.join(str(value) for value in filtered_values) + '\n')


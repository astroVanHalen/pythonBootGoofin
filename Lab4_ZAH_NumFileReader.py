##################################################
###	Title   - Number file reader
###	Author – Zac Huron
###	Date – 2/12/22
###     Description
###         This script will read values of file
###	    Details
###         1. Requires the os module
###         2. Requires the csv module
##################################################  


#import necessary modules
import csv
import os

info = []
num_list = []

# Set the file name
file_name = input("Enter file name: ")

# Change the working directory
file_directory = input("Enter file directory: ")
os.chdir(file_directory)

with open(file_name,'r') as file:
# get contents of the file
  info = csv.reader(file)

#info is a csv.reader variable type. Need to get it into a list
  temp_list = list(info)

#Side effect of bringing it into a list is that it takes the entire chunk
# of data as a single entry

#The list from above has one entry with is a list of the data
# The data is the first entry in that list
# Extract the data into a list and convert the string fields to integers
num_list = list(map(int,temp_list[0]))
print(num_list)


# Close the file, protect from corruption
file.close()

        

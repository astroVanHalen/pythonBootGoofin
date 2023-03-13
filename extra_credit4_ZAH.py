##################################################
###	Title- Extra Credit, Lab 4
###	Author – Zac Huron
###	Date – 2/12/22
###     Description
###        Find total entries, average, min, max, and standard deviation of 
###         item in .dat file
##################################################  


# import proper modules
import os
import csv
import statistics


# definitions
path = input("Enter filepath here: ")
file = open(path)
reader = csv.reader(file)
data = [ row for row in reader]

temp_list = list(data)

num_list = list(map(int,temp_list[0]))

# prints the list from the .dat file
print(num_list)

# defining a function to calculate average
def Average(list):
    avg = sum(num_list) / len(num_list)
    return avg

# Average function gave me problems with passing arguments.
# This fixed it.
average = Average(num_list)

# Run the functions to get information from data
with open(path) as file:
    reader = csv.reader(file)
    print("Number of values in list: ", len(num_list))
    print("Average value within the list: ",  average)
    print("Standard deviation of values is: ", statistics.stdev(num_list))
    print("Minimum value in list: ", min(num_list))
    print("Max value in list is: ", max(num_list))

    

# CLOSE THAT FILE, KID
file.close()



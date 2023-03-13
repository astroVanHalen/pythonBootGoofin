##############################################################
# LAB 7
# Zac Huron
# This lab modifies biggest.py, NumFileGen.py and NumFileRead.py
# scripts into functions that accept arguments.  
# 
##############################################################
import os
import random as rnd
import csv

'''
##############################################################
# This is my modification of the biggest.py file supplied for 
# lab 7. parameters are set to take an arbitrary amount of 
# arguments, later defined by the function itself.
##############################################################
def biggest(*x):
    """This function returns the max value in the list"""
    myList = []                                                             #Initialize a list
    for i in range(0,3):                                                    #This creates a loop to prompt the user
        user_input = float(input('Enter a number: '))                           #for a number three times, each time adding
        myList.append(user_input)                                               #it to our list
    num_inputs = len(myList)                                                #This returns the lengtch of the list as a variable
    max_val = myList[0]                                                     #Initialize our max_val variable and set it equal to first index
    for i in range(0,num_inputs,1):                                         #This loop iterates through the list, checking if the next
        if myList[i] > max_val:                                                 #number is greater than the current max_val and, if so,
            max_val = myList[i]                                                 #sets it as the new max_val
    print(f'The highest value according to my calculations is {max_val}')

biggest()
'''

##############################################################
# This function achieves the same goal, but is structured more
# closely to the original script.  This version takes in a set
# number of arguments
##############################################################
def biggest2(x,y,z):
    '''Takes user input for three values and returns the max'''
    myList = [x,y,z]
    myList.sort()
    max_value = myList[2]
    return max_value

mySecondList = []
a = float(input('Pick a numerical value: '))
b = float(input('Pick another numerical value: '))
c = float(input('Pick a third numerical1 value: '))
the_largest = biggest2(a,b,c)
print(f'The highest value according to my calculations is {the_largest}')


##############################################################
# The next section take the NumberFileGenerator and the 
# NumberFileReader and turns them into functions that can be
# called with two parameters for file_name and file_directory
# arguments.  
##############################################################
# initialize variables with user input
##############################################################
file_name = input('Enter filename: ')
file_directory = input('Enter absolute path to directory for the output file: ')
number = int(input('Enter a number between 1 and 100: '))

##############################################################
# Define the numFileGen with 2 parameters
##############################################################
def NumFileGen(name,directory,number):
    try:                                                      # Try/Except tests for valid directory for output
        os.chdir(directory)
        with open(name,'w') as file:
            for i in range(1,number):
                random_raw = rnd.randrange(0,100)
                random_final = int(random_raw)

                num_string = str(random_final)
                if i<number - 1:
                    num_string = num_string + ","        
                file.write(num_string)
    except:                                                   # Try/Except prints a message instead of throwing
        print('Directory not found')                          #     an error

##############################################################
# Here we define the numFileReader function with two parameters
##############################################################
def NumFileReader(fileName):
    info = []                                                 # initialize list
    num_list = []                                             # initialize list
    try:                                                      # try/except to test fileName existence
        with open(fileName,'r') as file:
            info = csv.reader(file)
            temp_list = list(info)
            num_list = list(map(int,temp_list[0]))
            print(num_list)
    except:
            print('File not found.')



NumFileGen(file_name,file_directory,number)                   # Call the function with arguments
NumFileReader(file_name)                                      # Call the function with arguments
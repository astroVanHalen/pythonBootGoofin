##############################################################
# LAB 10
# Zac Huron
# This lab further modifies biggest.py, NumFileGen.py and 
# NumFileRead.py to add error handling
##############################################################


import os
import random as rnd
import csv

##############################################################
# This function achieves the same goal, but is structured more
# closely to the original script.  This version takes in a set
# number of arguments
##############################################################
def biggest2(x,y,z):
    '''
    Takes user input for three values and returns the max value
    Parameters:
        x : integer
        y : integer
        z : integer
    
    Example:
        max = biggest(12,4,32)
        print(max)
        32
    '''
    myList = [x,y,z]
    myList.sort()
    max_value = myList[2]
    return max_value



##############################################################
# Define the NumFileGen with 2 parameters
##############################################################
def NumFileGen(name,directory,number):
        '''
    Uses the random.randrange() function to generate a list of 
    integers between 1-100.  The number of integers in the list
    is defined as an argument.
    Parameters:
        name(str): Name of file to be created
        directory(str): the directory in which to store the file
        number(int): Number of random integers in list
    Example:
        NumFileGen(Spam.py, /foo/bar, 42)
    '''

    try:                                                      # Try/Except tests for valid directory for output
        os.chdir(directory)
        if os.path.isfile('./'+ name):                        # Added conditional to check if file exists  
            print('File already exists.')
        else:
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
# Define the NumFile_Gen_safe with two parameters
##############################################################
def NumFile_Gen_safe(name,directory,number):
    try:
        os.chdir(directory)
        file_path = os.path.join(directory, name)
        if os.path.exists(file_path):
            print('File already exists.')
            overwrite = input('Do you wish to overwrite this file? [yes/no]')
            if overwrite.lower() == 'yes':
                with open(file_path, 'w') as file:
                    for i in range(1, number):
                        random_number = rnd.randint(0, 100)
                        if i < number - 1:
                            file.write(f'{random_number},')
                        else:
                            file.write(str(random_number))
            else:
                print('As you wish.')
        else:
            with open(file_path, 'w') as file:
                for i in range(1, number):
                    random_number = rnd.randint(0, 100)
                    if i < number - 1:
                        file.write(f'{random_number},')
                    else:
                        file.write(str(random_number))
    except FileNotFoundError:
        print('Directory not found')                       



##############################################################
# Here we define the numFileReader function with two parameters
##############################################################
def NumFileReader(fileName):
    '''
    Takes a filename that containts comma seperated values
    and returns a printed list of the integers from the file.
    Parameters:
        fileName(str): name of csv file
        
    Example:
        NumFileReader(foo.csv)
    '''
    info = []                                                 # initialize list
    num_list = []                                             # initialize list
    try:                                                      # try/except to test fileName existence
        with open(fileName,'r') as file:
            info = csv.reader(file)
            temp_list = list(info)
            try:                                              #   
                num_list = list(map(int,temp_list[0]))        #       
                print(num_list)                               #  Added try/except to check for non-integers 
            except:                                           #           
                print('Non-integer variables found in file.') #   
    except:
            print('File not found.')



import os
import random as rnd
import csv


##############################################################
# This function achieves the same goal, but is structured more
# closely to the original script.  This version takes in a set
# number of arguments
##############################################################
def biggest(x,y,z):
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
# Define the numFileGen with 2 parameters
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

    try:                                                    
        os.chdir(directory)
        with open(name,'w') as file:
            for i in range(1,number):
                random_raw = rnd.randrange(0,100)
                random_final = int(random_raw)

                num_string = str(random_final)
                if i<number - 1:
                    num_string = num_string + ","        
                file.write(num_string)
    except:                                                  
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
            num_list = list(map(int,temp_list[0]))
            print(num_list)
    except:
            print('File not found.')



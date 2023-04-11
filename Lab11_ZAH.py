##############################################################
# LAB 11
# Zac Huron
# 

##############################################################
import os
import random

def NumFileGen(name, directory, number):
    '''
    Uses the random.randrange() function to generate a list of 
    integers between 0-100.  The number of integers in the list
    is defined as an argument.
    Parameters:
        name(str): Name of file to be created
        directory(str): the directory in which to store the file
        number(int): Number of random integers in list
    Example:
        NumFileGen('Spam.py', '/foo/bar', 42)
    '''
    try:
        # Check if the number of values to be generated is less than zero
        if number <= 0:
            raise ValueError("The number of values to be generated cannot be less than zero.")


    # Check if the filename has any invalid characters
        elif any(name.startswith(c) for c in [' ', '.', '-', '_']) \
          or any(name.endswith(c) for c in [' ', '.', '-', '_']) \
          or any(c in name for c in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']):    
            raise ValueError("The filename is invalid.")
        

    # Check if the output file already exists
        elif os.path.exists(directory):
            print('File already exists.')
            overwrite = input('Do you wish to overwrite this file? [yes/no]')
            if overwrite.lower() == 'no':
                print('As you wish')
            else:
                    # Change to the specified directory
                os.chdir(directory)

                    # Generate random integers and write them to file
                with open(name, 'w') as file:
                        for i in range(number):
                            random_raw = random.randrange(0, 101)
                            random_final = int(random_raw)

                            num_string = str(random_final)
                            if i < number - 1:
                                num_string += ","
                            file.write(num_string)

    # print statements for individual errors, plus a catchall error
    except ValueError as e:
        print(f'ValueError: {e}')
    except FileExistsError as e:
        print(f'FileExistsError: {e}')
    except:
        print("An error occurred while generating the file.")
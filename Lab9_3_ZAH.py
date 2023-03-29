##############################################################
# LAB 9
# Zac Huron
# This lab uses biggest.py, NumFileGen.py and NumFileRead.py
# as modules.
# 
##############################################################

import Lab9                             # import Lab9 module


a = float(input('Pick a numerical value: '))
b = float(input('Pick another numerical value: '))
c = float(input('Pick a third numerical1 value: '))
x = Lab9.biggest(a,b,c)
print(f'The highest value according to my calculations is {x}')


file_name = input('Enter filename: ')
file_directory = input('Enter absolute path to directory for the output file: ')
number = int(input('Enter a number between 1 and 100: '))


Lab9.NumFileGen(file_name,file_directory,number)                   # Call the function with arguments
Lab9.NumFileReader(file_name)                                      # Call the function with arguments



help(Lab9) 

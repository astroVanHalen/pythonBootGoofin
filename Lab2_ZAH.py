	##################################################################
	###  	Lab 02
	###	    by Zachary Huron
	###	    Description – Take user input and manipulate the data then
	###		print the result
	##################################################################

# User input is converted to a float
x = float(input("Enter a numerical digit "))

part_b = (x+2.1)*5 #Define new variable for problem b

integer = int(part_b) #Define variable 'integer' as the integer part of 'part_b'

fractional = part_b - integer #Define variable 'factional' as the fractional part of 'part_b'

print(integer)      #print the integer and fractional variables defined for part c & d
print(fractional)

#This section was used to check variable type when testing.
#print(type(integer))
#print(type(fractional))

full_name = (input("Enter full name "))  #Get user to input full name

first = full_name.split()[0]        #
last = full_name.split()[-1]        #Take the full name and split it into two variables

print(full_name.upper())            #Print users full name in upper case
print(full_name.lower())            #Print users full name in lower case


#Print full name using f string and title case
message = f"First name:{full_name.split()[0].title()}\r\nLast name:{full_name.split()[-1].title()}" 
print(message)                                                              


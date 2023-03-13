##################################################################
###  	Title - Lab 03
###	    Author - Zachary Huron
###     Date - 02/02/2023
###	    Description – Explore working with lists
##################################################################
 
#Create list and print
ilike = ['python', 'alice_in_borderland', 'minecraft', 'soda_water', 'thrice']
print(ilike)

#Sort list- I chose reverse
ilike.reverse()

#Print the fourth item in the list.
print('The fourth item in the reverse-alphabetized list "ilike" is' ,ilike[4],'.')

#Append a sixth item on the list
ilike.append('tacos')

#Insert a seventh item, not at the end
ilike.insert(2, 'tattoos')

#Remove the fourth item

                # list.remove() could be used, but the item would need be named.
ilike.pop(3)    # In this instance, we use list.pop() to choose the arbitrary 4th 
                # item, as stated in the instructions.


#Final print for outomce of lab
print(ilike)
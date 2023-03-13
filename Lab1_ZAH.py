	##################################################################
	###  	Lab 01
	###	    by Zachary Huron
	###	    Description – this script will print out my first and last name using string 
	###		variables and using an f-string
	##################################################################

first_name = "Zac"
last_name = "Huron"
full_name = f"{first_name} {last_name}"

print(full_name)

print(f"Hello, {full_name.lower()}!")

print(f"Hello, {full_name.upper()}!")

message = f"Hello, {full_name.title()}!"
print(message)
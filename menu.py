print("Please choose an option from the menu below:")
print("1. Option 1")
print("2. Option 2")
print("3. Option 3")
print("4. Option 4")

choice = 0
while choice not in [1, 2, 3, 4]:
    choice = int(input("Enter your choice: "))

print("You selected option", choice)

if choice == 1:
    print("Running code for option 1")
elif choice == 2:
    print("Running code for option 2")
elif choice == 3:
    print("Running code for option 3")
else:
    print("Running code for option 4")

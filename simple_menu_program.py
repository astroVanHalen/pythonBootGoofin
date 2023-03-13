import sys

print ("This is a basic calc that will add, subtract, multiply, or divide two values")

#   Ask for two numbers
num1=float(input("Enter the first number "))
num2=float(input("Enter the second number "))

# Display basic menu
print("Enter 1 to Add")
print("Enter 2 to Subtract")
print("Enter 3 to Muiltiply")
print("Enter 4 to Divide")
print("Enter 0 to Quit")

# Validate menu selection
choice=int(input("Enter your choice: "))
while choice<0 or choice>4:
    choice=int(input("Invalid choice. Enter your choice: "))

# Execute the choice on selected two numbers
if choice==0:
    sys.exit()
if choice==1:
    answer=num1+num2
if choice==2:
    answer=num1-num2
if choice==3:
    answer=num1*num2
if choice==4:
    answer=num1/num2

# Display answer
print("The answer is ",answer,"." )
######################################################
## Lab7_Course Menu
## Zac Huron
## IT_Scripting
## Description: This lab uses dictionaries and for loops
##     to take user input for classes and return classes
##     available based on term and classes taken.
######################################################


# create a dictionary to hold the term and classes offered for each
term = {
    "Fall": ["NETC-121", "NETC-122", "NETC-180", "NETC-230", "NETA-155"],
    "Spring": ["NETC-121", "NETC-122", "NETC-170", "NETC-240", "NETC-280", "NETC-290", "IT-215"]
}

# create a dictionary to hold the prerequisites for each course--
# --because this dict is also used to validate user input for courses,
# the IT classes have been added here.  NET-290 did not name any prerquisites
prerequisites = {
    "IT-105": [],
    "IT-115": [],
    "IT-215": [],
    "NETC-121": [],
    "NETA-155": ["NETC-121", "IT-105", "IT-115"],
    "NETC-122": ["NETC-121"],
    "NETC-170": ["MGT-130", "NETC-121"],
    "NETC-180": ["NETC-122", "NETA-155"],
    "NETC-230": ["NETC-121"],
    "NETC-240": ["NETC-122", "NETA-155"],
    "NETC-280": ["ENG-101", "NETC-170"],
    "NETC-290": []
}

# create a variable for courses taken that will exist
# while this entire code is ran

courses_taken = []

##################################################################################
# function to display the courses taken by the student
# this funciton uses conditional statements to check if 
# uses has any courses and gives appropriate response

def display_courses():
    if not courses_taken:
        print("\nNo courses taken yet.")
    else:
        print("\nCourses taken:")
        for course in courses_taken:
            print("- " + course)

##################################################################################
# function to add a course to the list this function lists all major-specific
# courses then allows user to input courses  they have taken already. it also checks for
# duplicates
def add_course():
    for key in prerequisites:
        course_str = ", ".join(prerequisites)
    print("Here is a list of computer science courses: \n" + course_str)
    course = input("\nEnter course you have taken: ")
    if course in prerequisites.keys():
        if course not in courses_taken:
            courses_taken.append(course)
            print(course + " has been added.")
        else:
            print("\nCourse already in list.")
    else:
        print("\nInvalid course, try another")

##################################################################################
# function to remove a course from the list
# this funciton will display the users current listed
# courses and allows them to choose which to remove.
# If course they want removed isnt in the list, a 
# message will prompt them.
def remove_course():
    display_courses()
    course = input("\nEnter a course to remove: ")
    if course in courses_taken:
        courses_taken.remove(course)
        print('\n' + course, "has been removed.")
    else:
        print('\n' + course, "is not in the list of courses taken.")


##################################################################################
# a function to display the eligible courses for the student
# this function defines the next_term variable with user input and uses a conditional
# statement to validate the user input for term.  the .title() method is used to 
# format the user input.  To compute eligible courses, a for loop check within the
# term dict for the user input, then checks if what classes have all prereqs listed
# within courses_taken
#
def display_eligible_courses():
    next_term = input("\nEnter the next term you intend to register for (Fall or Spring): ")
    if next_term.lower() == 'fall' or next_term.lower() == 'spring':
        next_term = next_term.title()
    else:
        print('\nInvalid term.  Please enter either Fall or Spring')
        return
    available_courses = []
    for course in term[next_term]:
        if all(prerequisite in courses_taken for prerequisite in prerequisites[course]) and course not in courses_taken:
            available_courses.append(course)
    if available_courses:
        print("\nThe following courses are available:")
        for course in available_courses:
            print(course)
    else:
        print("\nNo courses are available for the selected term.")
                                
##################################################################################
# this is the code structured from the menu.py file.  Throught this file, the 
# use of \n has made print statements more readable for the user.  a 'while true' statement 
# allows this part to loop until choice '0' is selected and a 'break' is ran to force-end
# the loop.  the conditional statements check user input and runs the corresponding function
while True:
    print("\nWhat would you like to do?")
    print("1. Display courses taken.")
    print("2. Add a course taken.")
    print("3. Remove a course taken.")
    print("4. Display eligible courses.")
    print("0. Quit.")

    choice = input("Enter your choice: ")
    

    if choice == "1":
        display_courses()
    elif choice == "2":
        add_course()
    elif choice == "3":
        remove_course()
    elif choice == "4":
        display_eligible_courses()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")

##################################################################################
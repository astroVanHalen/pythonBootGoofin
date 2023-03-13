# initialize an empty list to hold the courses taken by the student
courses_taken = []

# a function to display the courses taken by the student
def display_courses():
    if not courses_taken:
        print("No courses taken yet.")
    else:
        print("Courses taken:")
        for course in courses_taken:
            print("- " + course)

# a function to add a course to the list
def add_course():
    course = input("Enter a course that you have taken: ")
    courses_taken.append(course)
    print(course, "has been added to the list of courses taken.")

# a function to remove a course from the list
def remove_course():
    display_courses()
    course = input("Enter a course to remove: ")
    if course in courses_taken:
        courses_taken.remove(course)
        print(course, "has been removed from the list of courses taken.")
    else:
        print(course, "is not in the list of courses taken.")

# ask the student for the next term they intend to register for
next_term = input("Enter the next term you intend to register for: ")

# a function to display the eligible courses for the student
def display_eligible_courses():
    course_type = input("Enter course type (NETC-XXX, NETA-155, IT-215): ")
    eligible_courses = []
    if course_type == "NETC-XXX":
        eligible_courses = ["NETC-101", "NETC-102", "NETC-103"]
    elif course_type == "NETA-155":
        eligible_courses = ["NETA-155"]
    elif course_type == "IT-215":
        eligible_courses = ["IT-215"]
    else:
        print("Invalid course type.")
    if eligible_courses:
        print("Eligible courses for", course_type + ":")
        for course in eligible_courses:
            if course not in courses_taken:
                print("- " + course)


# call functions based on user's input
while True:
    print("\nWhat would you like to do?")
    print("1. Display courses taken")
    print("2. Add a course taken")
    print("3. Remove a course taken")
    print("4. Enter next term")
    print("5. Display eligible courses")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_courses()
    elif choice == "2":
        add_course()
    elif choice == "3":
        remove_course()
    elif choice == "4":
        next_term = input("Enter the next term you intend to register for: ")
    elif choice == "5":
        display_eligible_courses()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

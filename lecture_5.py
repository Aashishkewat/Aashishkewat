#lecture 5
course = input("Enter course name: ")

if course == "BSCIT":
    percentage = int(input("Enter percentage: "))
    subject = input("Enter subject: ")
    
    if subject == "maths":
        print("You have selected maths.")
        print("You are in.")
    else:
        print("Sorry, you are not eligible for maths.")
else:
    print("Course not recognized.")
  

students = []

while True:
    print("\n===== Student Information System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll = input("Enter Roll Number: ")
        department = input("Enter Department: ")
        cgpa = input("Enter CGPA: ")

        student = {
            "Name": name,
            "Roll Number": roll,
            "Department": department,
            "CGPA": cgpa
        }

        students.append(student)
        print("\nStudent added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("\nNo student records found.")
        else:
            print("\n------ Student Details ------")
            for i, student in enumerate(students, start=1):
                print(f"\nStudent {i}")
                print(f"Name       : {student['Name']}")
                print(f"Roll No    : {student['Roll Number']}")
                print(f"Department : {student['Department']}")
                print(f"CGPA       : {student['CGPA']}")

    elif choice == "3":
        print("\nThank you!")
        break

    else:
        print("\nInvalid choice. Please try again.")
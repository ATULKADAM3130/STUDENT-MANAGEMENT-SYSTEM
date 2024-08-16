import student_database as std

students = std.load_from_file()

while True:
    choice = int(input("Enter 1 to Add Student\nEnter 2 to Delete Student\nEnter 3 to Update Student\nEnter 4 to Search Student\nEnter 5 to Display All Students\nEnter 6 to Exit\nChoose an option: "))

    if choice == 1:
        std.add_student(students)

    elif choice == 2:
        student_id = int(input("Enter ID of the student you want to delete: "))
        std.delete_stud(students, student_id)

    elif choice == 3:
        student_id = int(input("Enter ID of the student you want to update: "))
        std.update_student(students, student_id)

    elif choice == 4:
        student_id = int(input("Enter ID of the student you want to search: "))
        std.search_student(students, student_id)

    elif choice == 5:
        for student in students:
            print(student)

    elif choice == 6:
        std.save_to_file(students)
        print("EXIT")
        break

    else:
        print("Invalid option. Please choose again.")

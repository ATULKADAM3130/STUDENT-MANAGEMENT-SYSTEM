def add_student(stud):
    student_id = int(input("Enter ID of the student: "))
    name = input("Enter name of the student: ")
    age = int(input("Enter age of the student: "))
    grade = input("Enter grade of the student: ")
    data = [student_id, name, age, grade]
    stud.append(data)
    print("Student added successfully.")

def delete_stud(stud, student_id):
    for i in stud:
        if i[0] == student_id:
            stud.remove(i)
            print("Student data deleted successfully.")
            return
    print("Student with ID not found.")

def update_student(stud, student_id):
    for student in stud:
        if student[0] == student_id:
            c = input("Enter the key you want to update (name, age, grade): ")
            if c == 'name':
                student[1] = input("Enter updated name: ")
            elif c == 'age':
                student[2] = int(input("Enter updated age: "))
            elif c == 'grade':
                student[3] = input("Enter updated grade: ")
            else:
                print("Invalid key.")
            print("Student data updated successfully.")
            return
    print("Student with ID not found.")

def search_student(stud, student_id):
    for student in stud:
        if student[0] == student_id:
            print("Student found:", student)
            return
    print("Student with ID not found.")

def save_to_file(stud, filename="students.txt"):
    with open(filename, 'w') as file:
        for i in stud:
            file.write(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n")
    print("Data saved to file.")
    print("Current data in file:", stud)

def load_from_file(filename="students.txt"):
    stud = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                student = line.strip().split(',')
                student[0] = int(student[0])
                student[2] = int(student[2])
                student[3] = str(student[3])  
                stud.append(student)
    except FileNotFoundError:
        print("File not found. Starting with an empty list.")
    print("Data loaded from file:", stud)
    return stud

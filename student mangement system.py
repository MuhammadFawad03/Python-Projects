# Student Management System

students = []     

# 1. Add Student

def add_student():
    print("\n===== Add Student =====")

    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    marks = []

    print("Enter marks for 3 subjects:")

    for i in range(3):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

    print("\nStudent added successfully!")


# 2. Search Student

def search_student():
    print("\n===== Search Student =====")

    search = input("Enter student ID or name: ")

    found = False

    for student in students:

        # Search by ID
        if search.isdigit() and student["id"] == int(search):
            display_student(student)
            found = True

        # Search by name
        elif student["name"].lower() == search.lower():
            display_student(student)
            found = True

    if not found:
        print("Student not found.")



# Display One Student
def display_student(student):
    print("\n-------------------------")
    print("Student ID :", student["id"])
    print("Name       :", student["name"])
    print("Age        :", student["age"])
    print("Marks      :", student["marks"])


# 3. View All Students

def view_students():
    print("\n===== All Students =====")

    if len(students) == 0:
        print("No students available.")
        return

    for student in students:
        display_student(student)


# 4. Update Student
def update_student():
    print("\n===== Update Student =====")

    student_id = int(input("Enter student ID to update: "))

    for student in students:

        if student["id"] == student_id:

            print("\nStudent found!")

            student["name"] = input("Enter new name: ")
            student["age"] = int(input("Enter new age: "))

            new_marks = []

            print("Enter new marks:")

            for i in range(3):
                mark = float(input(f"Enter marks for subject {i + 1}: "))
                new_marks.append(mark)

            student["marks"] = new_marks

            print("\nStudent updated successfully!")
            return

    print("Student not found.")



# 5. Delete Student
def delete_student():
    print("\n===== Delete Student =====")

    student_id = int(input("Enter student ID to delete: "))

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            print("Student deleted successfully!")
            return

    print("Student not found.")



# 6. Calculate Student Average
def student_average():
    print("\n===== Student Average Marks =====")

    student_id = int(input("Enter student ID: "))

    for student in students:

        if student["id"] == student_id:

            total = sum(student["marks"])
            average = total / len(student["marks"])

            print("\nStudent Name :", student["name"])
            print("Marks        :", student["marks"])
            print("Average Marks:", round(average, 2))

            return

    print("Student not found.")



# Main Menu
def main():

    while True:

        print("\n====================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("====================================")
        print("1. Add Student")
        print("2. Search Student")
        print("3. View All Students")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Student Average")
        print("7. Exit")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            search_student()

        elif choice == "3":
            view_students()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            student_average()

        elif choice == "7":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("\nInvalid choice! Please enter 1-7.")


# ------------------------------------------
# Start Program
# ------------------------------------------
main()
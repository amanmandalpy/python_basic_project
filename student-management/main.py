import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")

    students.append({
        "id": student_id,
        "name": name,
        "age": age
    })

    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No students found.")
        return

    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"Age: {student['age']}"
        )


def search_student(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print(student)
            return

    print("Student not found.")


def update_student(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("New Name: ")
            student["age"] = input("New Age: ")
            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
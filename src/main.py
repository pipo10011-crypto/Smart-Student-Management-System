from database import Database

db = Database()

students = db.load_students()

print("=" * 40)
print(" Smart Student Management System ")
print("=" * 40)

name = input("Student Name: ")
age = int(input("Student Age: "))
department = input("Department: ")
level = int(input("Level: "))
gpa = float(input("GPA: "))

student = {
    "name": name,
    "age": age,
    "department": department,
    "level": level,
    "gpa": gpa
}

students.append(student)

db.save_students(students)

print("\nStudent saved successfully!")
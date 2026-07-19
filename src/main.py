from database import Database

db = Database()

while True:
    print("\n====== Smart Student Management ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "6":
        print("Goodbye!")
        break

    print("This feature will be implemented soon.")
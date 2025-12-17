def load_students():
    students = []
    try:
        with open("students.txt", "r") as f:
            for line in f:
                roll, name, marks = line.strip().split(",")
                students.append({
                    "roll": roll,
                    "name": name,
                    "marks": marks
                })
    except FileNotFoundError:
        with open("students.txt","w") as f:
            pass
        print("Student data file created.")
    return students


def save_students(students):
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['roll']},{s['name']},{s['marks']}\n")


def add_student(students):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })

    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\nRecord containing Student details")
    for s in students:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Marks: {s['marks']}")


def search_student(students):
    roll = input("Enter roll number to search: ")

    for s in students:
        if s["roll"] == roll:
            print(f"Found → Roll: {s['roll']} | Name: {s['name']} | Marks: {s['marks']}")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


main()

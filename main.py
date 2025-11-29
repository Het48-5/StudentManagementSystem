import json

def load_data():
    try:
        with open("students.txt", "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open("students.txt", "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll no: ")
    course = input("Enter course: ")

    data = load_data()
    data.append({"name": name, "roll": roll, "course": course})
    save_data(data)
    print("Student added!")

def view_students():
    data = load_data()
    for s in data:
        print(s)

def search_student():
    roll = input("Enter roll to search: ")
    data = load_data()
    for s in data:
        if s["roll"] == roll:
            print("Found:", s)
            return
    print("Student not found")

def delete_student():
    roll = input("Enter roll to delete: ")
    data = load_data()
    new_data = [s for s in data if s["roll"] != roll]
    save_data(new_data)
    print("Deleted student (if existed).")

while True:
    print("\n1 Add\n2 View\n3 Search\n4 Delete\n5 Exit")
    choice = input("Choose: ")

    if choice == "1": add_student()
    elif choice == "2": view_students()
    elif choice == "3": search_student()
    elif choice == "4": delete_student()
    else: break

# attendence tracker
student_name = ""
student_status = ""

def show_menu():
    print("\n----attendence tracker----")
    print("1. add attendence")
    print("2. view attendence")
    print("3. exit")

def add_attendence():
    global student_name
    global student_status

    student_name = input("enter student name: ")
    student_status = input("enter status (present/absent): ")

    print("attendence added sucessfully.")

def view_attendence():
    if student_name == "":
        print("no attendence record found")
    else:
        print("\n----attendence record----")
        print(student_name,"-", student_status)

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_attendence()
        elif choice == "2":
            view_attendence()
        elif choice == "3":
            print("exiting the programm")
            break
        else:
            print("Invalid choice, try again")

# =======
# attendence tracker
student_name = ""
student_status = ""

def show_menu():
    print("\n----attendence tracker----")
    print("1. add attendence")
    print("2. view attendence")
    print("3. exit")

def add_attendence():
    global student_name
    global student_status

    student_name = input("enter student name: ")
    student_status = input("enter status (present/absent): ")

    print("attendence added sucessfully.")

def view_attendence():
    if student_name == "":
        print("no attendence record found")
    else:
        print("\n----attendence record----")
        print(student_name,"-", student_status)

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_attendence()
        elif choice == "2":
            view_attendence()
        elif choice == "3":
            print("exiting the programm")
            break
        else:
            print("Invalid choice, try again")
main()
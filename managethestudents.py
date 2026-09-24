def get_users_selection():
    print("Select an option:")
    print("1. Add student(s)")
    print("2. Add course(s)")
    print("3. Add mark(s)")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        add_course()
    elif choice == "3":
        add_mark()
    else:
        print("Invalid choice.")
    return choice


STUDENTS = []
def add_student():
    quantity = int(input("How many students do you want to add?"))
    for _ in range(quantity):
        name = str(input("Enter student name: "))
        student_id = str(input("Enter student id: "))
        dob = str(input("Enter student date of birth: "))
        student = {"name": name, "student_id": student_id, "dob": dob}
        STUDENTS.append(student)
    return student

COURSES = []
def add_course():
    quantity = int(input("How many courses do you want to add?"))
    for _ in range(quantity):
        course_name = str(input("Enter course name: "))
        course_id = str(input("Enter course id: "))
        course = {"course_name": course_name, "course_id": course_id}
        COURSES.append(course)
    return course

MARKS = []
def add_mark():
    quantity = int(input("How many marks do you want to add?"))
    for _ in range(quantity):
        student_name = str(input("Enter student name: "))
        student_id = str(input("Enter student id: "))
        course_id = str(input("Enter course id: "))
        mark = float(input("Enter mark: "))
        mark_entry = {"student_name": student_name, "student_id": student_id, "course_id": course_id, "mark": mark}
        MARKS.append(mark_entry)
    return mark_entry

def main():
    while True:
        choice = get_users_selection()
        if choice == "1":
            print("Students added:")
            for student in STUDENTS:
                print(student)
        elif choice == "2":
            print("Courses added:")
            for course in COURSES:
                print(course)
        elif choice == "3":
            print("Marks added:")
            for mark in MARKS:
                print(mark)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    

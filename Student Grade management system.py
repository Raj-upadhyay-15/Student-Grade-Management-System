# Initialize an empty dictionary to store student data
students_grades = {}

# Function to add a student
def add_student(student_id, name):
    if student_id in students_grades:
        print(f"Student with ID {student_id} already exists.")
    else:
        students_grades[student_id] = {'name': name, 'grades': {}}
        print(f"Student {name} added successfully.")

# Function to add/update grades for a student
def add_grade(student_id, subject, grade):
    if student_id in students_grades:
        students_grades[student_id]['grades'][subject] = grade
        print(f"Grade {grade} for {subject} added/updated for {students_grades[student_id]['name']}.")
    else:
        print(f"Student with ID {student_id} does not exist.")

# Function to display all students and their grades
def display_grades():
    if not students_grades:
        print("No students in the system.")
    else:
        print("\nStudent Grades:")
        for student_id, info in students_grades.items():
            print(f"ID: {student_id}, Name: {info['name']}, Grades: {info['grades']}")

# Function to calculate the average grade for a student
def calculate_average(student_id):
    if student_id in students_grades:
        grades = students_grades[student_id]['grades'].values()
        if grades:
            average = sum(grades) / len(grades)
            print(f"Average grade for {students_grades[student_id]['name']} is {average:.2f}.")
        else:
            print(f"No grades available for {students_grades[student_id]['name']}.")
    else:
        print(f"Student with ID {student_id} does not exist.")

# Main menu function
def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Display Grades")
        print("4. Calculate Average Grade")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            add_student(student_id, name)
        elif choice == '2':
            student_id = input("Enter student ID: ")
            subject = input("Enter subject name: ")
            grade = float(input("Enter grade: "))
            add_grade(student_id, subject, grade)
        elif choice == '3':
            display_grades()
        elif choice == '4':
            student_id = input("Enter student ID to calculate average: ")
            calculate_average(student_id)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

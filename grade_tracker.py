def input_grades(subject):
    """Get grades from the user for a specific subject."""
    grades = []
    while True:
        grade_input = input(f"Enter the grade for {subject} (or 'done' to finish): ")
        if grade_input.lower() == 'done':
            break
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
    return grades

def calculate_average(grades):
    """Calculate the average of a list of grades."""
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0

def main():
    subjects = ['Math', 'Science', 'English', 'History']
    student_grades = {}

    for subject in subjects:
        grades = input_grades(subject)
        student_grades[subject] = grades

    print("\nStudent Grades:")
    for subject, grades in student_grades.items():
        average = calculate_average(grades)
        print(f"{subject}: Grades - {grades}, Average - {average:.2f}")

if __name__ == "__main__":
    main()

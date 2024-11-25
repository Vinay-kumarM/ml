# Develop a program to read the student details like Name, USN, and Marks in three subjects.
# Display the student details, total marks and percentage with suitable messages.
def get_student_details():
    try:
        # Reading student details
        name = input("Enter the student's name: ")
        usn = input("Enter the student's USN: ")

        # Reading marks with validation
        marks = []
        for i in range(3):
            mark = float(
                input(f"Enter marks for subject {i + 1} (out of 100): "))
            if not (0 <= mark <= 100):
                raise ValueError("Marks should be between 0 and 100.")
            marks.append(mark)

        return name, usn, marks
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None


def calculate_results(marks):
    try:
        total_marks = sum(marks)
        percentage = total_marks / 3
        return total_marks, percentage
    except Exception as e:
        print(f"Error in calculating results: {e}")
        return None, None


def display_student_details(name, usn, total_marks, percentage):
    try:
        print("\n--- Student Details ---")
        print(f"Name       : {name}")
        print(f"USN        : {usn}")
        print(f"Total Marks: {total_marks}/300")
        print(f"Percentage : {percentage:.2f}%")
    except Exception as e:
        print(f"Error in displaying student details: {e}")


# Main program
if __name__ == "__main__":
    try:
        details = get_student_details()
        if details:
            name, usn, marks = details
            total_marks, percentage = calculate_results(marks)
            if total_marks is not None and percentage is not None:
                display_student_details(name, usn, total_marks, percentage)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

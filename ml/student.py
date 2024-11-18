class Student:
    def __init__(self):
        # Initialize student name, USN, marks list, and total marks
        self.name = input("Enter student name: ")
        self.usn = input("Enter student USN: ")
        self.marks = []  # List to store marks of 3 subjects
        self.total = 0  # To store total marks
        self.percentage = 0  # To store percentage

    def getMarks(self):
        # Read marks into the list
        for i in range(3):
            while True:
                try:
                    mark = float(input(f"Enter marks for subject {i + 1}: "))
                    if mark < 0 or mark > 100:
                        raise ValueError("Marks should be between 0 and 100.")
                    self.marks.append(mark)
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please enter valid marks.")

    def calculateTotalAndPercentage(self):
        # Calculate total marks and percentage
        self.total = sum(self.marks)
        self.percentage = self.total / len(self.marks)

    def display(self):
        # Display the score card details
        print("\n------ Score Card ------")
        print(f"Name: {self.name}")
        print(f"USN: {self.usn}")
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {self.total}")
        print(f"Percentage: {self.percentage:.2f}%")
        print("------------------------")


# Main program logic without additional functions
try:
    # Create a Student object
    student = Student()

    # Get the marks from the user
    student.getMarks()

    # Calculate total marks and percentage
    student.calculateTotalAndPercentage()

    # Display the scorecard
    student.display()

except Exception as e:
    print(f"An unexpected error occurred: {e}")

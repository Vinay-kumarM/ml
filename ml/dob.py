# b. Develop a program to read the name and year of birth of a person. Display whether the person
# is a senior citizen or not.
from datetime import datetime


def get_person_details():
    try:
        name = input("Enter the person's name: ")
        year_of_birth = int(input("Enter the year of birth (YYYY): "))

        # Validating year of birth
        current_year = datetime.now().year
        if year_of_birth < 1900 or year_of_birth > current_year:
            raise ValueError(
                "Year of birth should be between 1900 and the current year.")

        return name, year_of_birth
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None


def determine_senior_citizen(year_of_birth):
    try:
        current_year = datetime.now().year
        age = current_year - year_of_birth

        # Determining senior citizen status
        is_senior = age >= 60
        return age, is_senior
    except Exception as e:
        print(f"Error in determining senior citizen status: {e}")
        return None, None


def display_status(name, age, is_senior):
    try:
        print("\n--- Person Details ---")
        print(f"Name: {name}")
        print(f"Age : {age}")
        if is_senior:
            print("Status: Senior Citizen")
        else:
            print("Status: Not a Senior Citizen")
    except Exception as e:
        print(f"Error in displaying details: {e}")


# Main program
if __name__ == "__main__":
    try:
        details = get_person_details()
        if details:
            name, year_of_birth = details
            age, is_senior = determine_senior_citizen(year_of_birth)
            if age is not None and is_senior is not None:
                display_status(name, age, is_senior)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

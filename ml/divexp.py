def DivExp(a, b):
    try:
        # Assertion to check if 'a' is greater than 0
        assert a > 0, "The value of 'a' must be greater than 0."

        # Raise an exception if 'b' is zero
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")

        # Perform division
        c = a / b
        return c
    except AssertionError as e:
        print(f"Assertion Error: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    try:
        # Read two values from the console
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        
        # Call the DivExp function
        result = DivExp(a, b)
        
        if result is not None:
            print(f"The result of {a} / {b} is: {result:.2f}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main program
if __name__ == "__main__":
    main()

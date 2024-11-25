class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"


def add_complex(c1, c2):
    try:
        # Adding two complex numbers
        real_part = c1.real + c2.real
        imag_part = c1.imag + c2.imag
        return Complex(real_part, imag_part)
    except AttributeError as e:
        print(f"Error: Invalid complex number objects provided. {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def read_complex():
    try:
        real = float(input("Enter the real part: "))
        imag = float(input("Enter the imaginary part: "))
        return Complex(real, imag)
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter numeric values.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    try:
        n = int(input("Enter the number of complex numbers (N >= 2): "))
        if n < 2:
            raise ValueError("N must be at least 2.")

        complex_numbers = []
        for i in range(n):
            print(f"\nEnter complex number {i + 1}:")
            complex_num = read_complex()
            if complex_num:
                complex_numbers.append(complex_num)

        # Summing all complex numbers
        total = complex_numbers[0]
        for i in range(1, n):
            total = add_complex(total, complex_numbers[i])

        print(f"\nThe sum of the {n} complex numbers is: {total}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the main program
if __name__ == "__main__":
    main()

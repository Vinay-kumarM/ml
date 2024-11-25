# . Develop a program to generate Fibonacci sequence of length (N). Read N from the console.
def generate_fibonacci_sequence(n):
    try:
        if n <= 0:
            raise ValueError(
                "The length of the Fibonacci sequence must be a positive integer.")

        # Generating the Fibonacci sequence
        sequence = [0, 1]
        for _ in range(2, n):
            sequence.append(sequence[-1] + sequence[-2])

        return sequence[:n]  # Return only up to the required length
    except Exception as e:
        print(f"Error in generating the Fibonacci sequence: {e}")
        return []


def main():
    try:
        n = int(input("Enter the length of the Fibonacci sequence (N): "))
        fibonacci_sequence = generate_fibonacci_sequence(n)

        if fibonacci_sequence:
            print(f"Fibonacci sequence of length {n}: {fibonacci_sequence}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the main program
if __name__ == "__main__":
    main()

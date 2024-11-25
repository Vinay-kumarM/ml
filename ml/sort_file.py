# Develop a program to sort the contents of a text file and write the sorted contents into a separat
# text file.
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def sort_lines(content):
    try:
        # Sorting the lines in alphabetical order
        sorted_content = sorted(content)
        return sorted_content
    except Exception as e:
        print(f"Error in sorting lines: {e}")
        return None


def write_sorted_file(sorted_content, output_file_path):
    try:
        with open(output_file_path, 'w') as file:
            file.writelines(sorted_content)
        print(f"Sorted content has been written to '{output_file_path}'")
    except Exception as e:
        print(f"Error in writing to the file: {e}")


def main():
    try:
        input_file_path = input("Enter the path of the input text file: ")
        output_file_path = input("Enter the path of the output text file: ")

        content = read_file(input_file_path)

        if content:
            sorted_content = sort_lines(content)

            if sorted_content:
                write_sorted_file(sorted_content, output_file_path)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the main program
if __name__ == "__main__":
    main()

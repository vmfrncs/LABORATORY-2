def main():
    """Prompt the user for a filename and allow them to read specific lines."""
    # Prompt the user for a filename
    filename = input("Enter the filename: ")

    # Try to read the file and store lines in a list
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist. Please check the filename and try again.")
        return

    # Get the number of lines in the file
    num_lines = len(lines)
    print(f"The file has {num_lines} lines.")

    while True:
        # Prompt the user for a line number
        try:
            line_number = int(input("Enter a line number (0 to quit): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # If the input is 0, quit the program
        if line_number == 0:
            print("Exiting the program.")
            break

        # Check if the line number is within range
        if 1 <= line_number <= num_lines:
            # Print the line associated with that number
            print(lines[line_number - 1].strip())
        else:
            print(f"Invalid input. Please enter a number between 1 and {num_lines}.")

if __name__ == "__main__":
    main()

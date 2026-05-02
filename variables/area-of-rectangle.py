def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt).strip())

            if value <= 0:
                print("Please enter a positive number.")
                continue

            return value

        except ValueError:
            print("Invalid input!")

def main():
    """
    Main function to run the program.
    Prompts for two numbers, calculates their sum, and prints the result.
    """
    # Prompt the user for the first and second numbers
    length = get_positive_number("Enter the length of the rectangle: ")
    width = get_positive_number("Enter the width of the rectangle: ")

    # Calculate the total area
    total = length * width
    
    # Display the result to the user
    print(f"The area of the rectangle is: {total}")

# Ensure the main function runs only if this script is executed directly
if __name__ == "__main__":
    main()
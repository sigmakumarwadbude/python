def get_number(prompt):
    """
    Prompts the user for a number and handles validation.
    Keeps asking until a valid integer is provided.
    
    Args:
        prompt (str): The text to display to the user.
        
    Returns:
        int: The validated integer entered by the user.
    """
    while True:
        # Get input from the user and remove leading/trailing whitespace
        user_input = input(prompt).strip()

        # Check if the user just pressed Enter without typing anything
        if not user_input:
            print("Input cannot be empty. Please enter a number.")
            continue

        # Try to convert the input to an integer
        try:
            return int(user_input)
        except ValueError:
            # If conversion fails, catch the error and ask again
            print("Invalid input! Please enter a valid number.")

def main():
    """
    Main function to run the program.
    Prompts for two numbers, calculates their sum, and prints the result.
    """
    # Prompt the user for the first and second numbers
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    # Calculate the total sum
    total = num1 + num2
    
    # Display the result to the user
    print(f"Sum of {num1} and {num2} is: {total}")

# Ensure the main function runs only if this script is executed directly
if __name__ == "__main__":
    main()

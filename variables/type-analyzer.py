def analyze(value):
    """
    Analyze and display type and specific insights for a given value.
    
    Args:
        value (any): The input value to be analyzed.
    """
    # Print the header for the analysis output
    print("\n🔍 Analysis Result")
    print("-" * 40)

    # Display the value itself and its core Python type
    print(f"Value : {value}")
    print(f"Type  : {type(value).__name__}")

    # Extra insights: provide specific details based on the exact type of the value
    if isinstance(value, str):
        # String insights: show length and an uppercase version
        print(f"Length: {len(value)}")
        print(f"Upper : {value.upper()}")

    elif isinstance(value, int):
        # Integer insights: check if the number is even
        print(f"Even  : {value % 2 == 0}")

    # TODO: Add more type insights (float, list, dict, set, etc.)

    elif value is None:
        # Explicit handling for NoneType
        print("This is a None value")

    # Print the footer line to close the analysis block
    print("-" * 40)


def parse_input(user_input):
    """
    Try to infer and convert a raw string input into a specific Python type.
    Falls back to returning the original string if no conversion matches.
    
    Args:
        user_input (str): The raw string input from the user.
        
    Returns:
        any: The converted value (e.g., int) or the original string.
    """
    # Try converting to an integer first
    try:
        return int(user_input)
    except ValueError:
        # If it fails, ignore the error and move to the next check
        pass

    # TODO: Add more type conversions (float, list, dict, set, etc.)

    # Fallback: if no conversion succeeded, return the raw string
    return user_input


def main():
    """
    Main execution loop for the Type Analyzer tool.
    Continuously prompts the user for input until they choose to exit.
    """
    # Print the welcome message and instructions
    print("🧠 Type Analyzer Tool")
    print("Type 'exit' to quit\n")

    # Start an infinite loop to keep the tool running
    while True:
        # Prompt user and strip trailing/leading whitespace
        user_input = input("Enter a value: ").strip()

        # Check for the exit command (case-insensitive)
        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        # Check if the user just pressed enter without typing anything
        if not user_input:
            print("❌ Input cannot be empty")
            continue

        # Parse the input to guess its true type
        value = parse_input(user_input)
        
        # Run the analysis on the parsed value
        analyze(value)


# Standard boilerplate to run the main function when the script is executed
if __name__ == "__main__":
    main()
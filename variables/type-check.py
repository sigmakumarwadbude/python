"""
Type Check

This script demonstrates the usage of various built-in Python data types
and how to identify them using the `type()` function.
"""

def show(value):
    """
    Helper function to print a value and its corresponding type in a formatted way.
    
    Args:
        value (any): The value to display and check the type of.
    """
    print(f"Value: {str(value):<15} | Type: {type(value).__name__}")

def main():
    """
    Main function that initializes variables of different types and calls
    the show() function to display their values and types.
    """
    # Integer: whole numbers without a fractional component
    my_int = 42
    show(my_int)

    # Float: numbers that contain a decimal point
    my_float = 3.14
    show(my_float)

    # String: a sequence of characters enclosed in quotes
    my_str = "Hello, Python!"
    show(my_str)

    # Boolean: represents truth values True or False
    my_bool = True
    show(my_bool)

    # List: an ordered, mutable collection of items
    my_list = [1, 2, 3]
    show(my_list)

    # Tuple: an ordered, immutable collection of items
    my_tuple = (1, 2, 3)
    show(my_tuple)

    # Dictionary: an unordered collection of key-value pairs
    my_dict = {"name": "Alice"}
    show(my_dict)

    # Set: an unordered collection of unique items
    my_set = {1, 2, 3}
    show(my_set)

    # NoneType: represents the absence of a value
    my_none = None
    show(my_none)

# Standard boilerplate to call the main() function to begin the program
if __name__ == "__main__":
    main()

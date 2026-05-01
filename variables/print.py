"""
Interactive script that collects and validates a user's name and age.

Validation rules:
- Name must not be empty.
- Age must be a numeric value between 1 and 120 (inclusive).

After successful validation, the script prints a summary sentence.
"""

# Prompt until a non-empty name is provided.
while True:
    name = input("Please enter your Name: ").strip()
    if name:
        break
    print("Name cannot be empty. Please enter a valid name.")

# Prompt until a valid numeric age in the allowed range is provided.
while True:
    age_input = input("Please enter your age: ").strip()
    if not age_input.isdigit():
        print("Age must be a valid number.")
        continue

    age = int(age_input)
    if 1 <= age <= 120:
        break

    print("Age must be between 1 and 120.")

# Display the validated user information.
print(f"My name is {name} and I am {age} years old")

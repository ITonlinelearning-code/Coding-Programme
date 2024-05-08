# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Display the string manipulation menu
print("\nString Manipulation Menu:")
print("1. Convert to uppercase")
print("2. Convert to lowercase")
print("3. Slice the string")
print("4. Calculate string length")
print("5. Loop through characters")

# Prompt the user to enter their choice
choice = int(input("Enter your choice (1-5): "))

# Perform the selected string manipulation
if choice == 1:
    result = input_string.upper()
    print("Uppercase:", result)
elif choice == 2:
    result = input_string.lower()
    print("Lowercase:", result)
elif choice == 3:
    start = int(input("Enter start index: "))
    end = int(input("Enter end index: "))
    result = input_string[start:end]
    print("Sliced string:", result)
elif choice == 4:
    length = len(input_string)
    print("String length:", length)
elif choice == 5:
    print("Characters:")
    for char in input_string:
        print(char)
else:
    print("Invalid choice.")
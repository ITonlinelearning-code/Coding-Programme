# Prompt the user for input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
occupation = input("Enter your occupation: ")

# Concatenate first name and last name
full_name = first_name + " " + last_name

# Create profile description using string formatting
profile_desc = f"{full_name} is {age} years old, lives in {city}, and works as a {occupation}."

# Add escape characters to include quotation marks and a new line
profile_info = "\"Profile Information:\"\n" + profile_desc

# Use string methods to modify the full name and profile description
modified_name = full_name.upper()
modified_desc = profile_info.replace("a", "an") if occupation.startswith(("a", "e", "i", "o", "u")) else profile_info

# Display the user profile
print("===== User Profile =====")
print(modified_name)
print(modified_desc)
print("========================")
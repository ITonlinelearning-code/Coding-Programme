import random

# Generating a random number between 1 and 100
random_number = random.randint(1, 100)

# Printing the random number along with its data type
print("Random Number:", random_number)
print("Data Type:", type(random_number))

# Defining multi-word variables
multiWordVariableCamelCase = "ThisIsCamelCase"
multi_word_variable_pascal_case = "ThisIsPascalCase"
multi_word_variable_snake_case = "this_is_snake_case"

# Type conversion examples
float_number = float(random_number)
complex_number = complex(random_number)

print("Random Number as Float:", float_number)
print("Data Type after Conversion to Float:", type(float_number))

print("Random Number as Complex:", complex_number)
print("Data Type after Conversion to Complex:", type(complex_number))

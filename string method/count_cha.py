# Input string
input_string = "Hell0 Subhodip ! 91262879826 * # welcome to pYtHoN"

# Initialize counters
uppercase_count = 0
lowercase_count = 0
number_count = 0
special_count = 0

# Iterate over each character in the string
for char in input_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        number_count += 1
    elif not char.isspace():  # Special characters (excluding spaces)
        special_count += 1

# Print the counts
print(f"UpperCase: {uppercase_count}")
print(f"LowerCase: {lowercase_count}")
print(f"NumberCase: {number_count}")
print(f"SpecialCase: {special_count}")

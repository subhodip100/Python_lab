""" Using input function take two number and then swap the number
Lab_Week1_Day 3_12_19_2024_8506
"""

# Taking two numbers as input
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

# Swapping the numbers using a temporary variable
a, b = b, a

# Output the swapped numbers
print(f"After swapping: First number is = {a}, Second number is = {b}")

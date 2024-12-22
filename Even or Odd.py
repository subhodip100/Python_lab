"""Check if the number is even or odd using a ternary operator
Lab_Week1_Day 3_12_19_2024_8506

"""

# Taking input from the user
number = int(input("Enter a number: "))
# Using ternary operator to check if the number is even or odd
result = "Even" if number % 2 == 0 else "Odd"
# Output the result
print(f"The number is {result}.")

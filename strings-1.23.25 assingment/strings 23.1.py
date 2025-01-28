'''Lab_Week_2_day3_strings_01_23_2025_8506
Assignment:'''



# Given string
string = "To change the overall look of your document. To change the look available in the gallery"

# Normalize the case and split the string into words
words = string.lower().replace(".", "").split()

# Create a dictionary to store word counts
word_counts = {}

# Count occurrences of each word
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Print the word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")

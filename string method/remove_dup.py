# Input string
input_string = "String and String Function"

# Function to remove duplicate words while maintaining order
def remove_duplicate_words(s):
    seen = set()
    result = []
    for word in s.split():
        if word not in seen:
            seen.add(word)
            result.append(word)
    return ' '.join(result)

# Removing duplicate words
output_string = remove_duplicate_words(input_string)
print(f"Output: {output_string}")

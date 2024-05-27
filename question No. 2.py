# String operations in Python

# Sample string
my_string = "This is a sample string"

# 1. Length of the string
string_length = len(my_string)
print("Length of the string:", string_length)

# 2. Splitting the string
words = my_string.split()  # Split by spaces
print("Split string into words:", words)

# Splitting by a delimiter
split_by_s = my_string.split('s')
print("Split string by 's':", split_by_s)

# 3. Joining the string
joined_string = " ".join(words)  # Join words with spaces
print("Joined string:", joined_string)

# 4. Accessing characters in the string
first_char = my_string[0]
last_char = my_string[-1]
third_char = my_string[2]  # Indexing starts from 0

print("First character:", first_char)
print("Last character:", last_char)
print("Third character:", third_char)

# Slicing a substring
substring = my_string[4:10]  # From index 4 (inclusive) to 10 (exclusive)
print("Substring:", substring)

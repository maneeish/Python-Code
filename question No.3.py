# List operations in Python

# Sample list of numbers
numbers = [5, 10, 3, 12, 1, 7]

# 1. Find the smallest number
smallest = min(numbers)
print("Smallest number:", smallest)

# 2. Find the largest number
largest = max(numbers)
print("Largest number:", largest)

# 3. Multiply all the items in the list
product = 1
for num in numbers:
  product *= num
print("Product of all numbers:", product)

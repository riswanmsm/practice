# Input the first value.
number = largest_number = int(input("Enter a number or type 0 to stop: "))

# If the number is not equal to 0, continue.
while number:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

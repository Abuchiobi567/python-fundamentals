# Ask the user to enter numbers without any spaces or commas
number_string = input("Enter some single-digit numbers with no spaces: ")

# Check if the input is valid
if number_string.isdigit():  # Make sure it only contains numbers
    total = 0  # Start with a sum of 0

    # Go through each character in the input and add it to the total
    for digit in number_string:
        total += int(digit)  # Convert each character to a number and add to total

    # Show the total sum
    print("The sum of the digits is:", total)
else:
    # If the input isn't valid, show an error message
    print("Please only enter numbers without spaces or other characters.")
# This function checks whether a string is a palindrome
def is_palindrome(strng):
    strng = strng.lower()  # Converting string to lowercase
    strng = ''.join(c for c in strng if c.isalnum())  # Remove non-alphanumeric characters
    return strng == strng[::-1]  # Checking if string is equal to its reverse
# This function finds the most frequent letter or digit in a string
def most_frequent_letter_or_digit(strng):
    strng = strng.upper()  # Convert string to uppercase
    counts = {}  # Initializing empty dictionary to store character counts
    for c in strng:
        if c.isalnum():
            counts[c] = counts.get(c, 0) + 1  # Adding 1 to character count or initialize count to 0
    max_count = max(counts.values())  # Finding the maximum count
    for c in counts:
        if counts[c] == max_count:
            return c  # Returning the character with the maximum count

# This function counts the number of letters, spaces, and digits in a string
def count_letters_spaces_digits(strng):
    counts = {'letters': 0, 'spaces': 0, 'digits': 0}  # Initialize counts to 0
    for c in strng:
        if c.isalpha():
            counts['letters'] += 1  # Increment letter count
        elif c.isspace():
            counts['spaces'] += 1  # Incrementing the space count
        elif c.isdigit():
            counts['digits'] += 1  # Incrementing the digit count
    return counts  # Returning the counts dictionary

# Main function is used to test the three functions
def main():
    user_input  = input("Enter a string: ")  # Prompting user to enter a string
    if is_palindrome(user_input):
        print("True")  # Printing True if string is a palindrome
    else:
        print("False")  # Printing False if string is not a palindrome
    print("In UpperCase Format:",user_input.upper())  # Print the string in uppercase format
    print("The most frequent letter/digit is:", most_frequent_letter_or_digit(user_input))#Print the most frequent letter/digit in the string
    counts = count_letters_spaces_digits(user_input) 
    print("Letter count:", counts['letters'])#Count the number of letters
    print("Space count:", counts['spaces'])#Count the number of spaces
    print("Digit count:", counts['digits'])#Count the number of digits

# Calling the main function if the script is run directly
if __name__ == '__main__':
    main()

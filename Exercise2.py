import math
# Defining a function to check for prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Defining a function to check for non-prime numbers between two given integers
def non_primes_between(start, end):
    if start > end:
        start, end = end, start
    non_primes = []
    for n in range(start, end+1):
        if not is_prime(n):
            non_primes.append(n)
    return non_primes

# Defining a main function to interact with the user and call the other functions
def main():
    # Looping until the user enters valid inputs
    while True:
        try:
            # Geting two positive integers from the user
            start_num = int(input("Enter a positive integer: "))
            end_num = int(input("Enter another positive integer: "))
            if start_num <= 0 or end_num <= 0:
                raise ValueError
            break
        except ValueError:
            # Printing an error message if the user enters invalid input
            print("Invalid input. Please enter positive integers.")
    
    # Geting the non-prime numbers between the user's input and print them
    non_primes = non_primes_between(start_num, end_num)
    print("Non-prime numbers between", start_num, "and", end_num, "are:")
    for i, n in enumerate(non_primes):
        print(n, end=' ')
        if (i+1) % 10 == 0:
            print()
    if len(non_primes) % 10 != 0:
        print()

# Calling the main function if the script is run as the main program
if __name__ == '__main__':
    main()

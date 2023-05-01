# Defining a function to display employees by pay range
def display_employee_by_pay_range(employee_list, min_pay, max_pay):
    # Createing a list to store matching employees
    matching_employees = []
    # Iterating over all employees
    for employee in employee_list:
        # Unpacking employee tuple
        name, position, pay = employee
        # Convert pay to integer
        pay = int(float(pay))
        # Check if employee pay is within range
        if min_pay <= pay <= max_pay:
            # Add matching employees to list
            matching_employees.append(employee)
    # If no matching employees, print message
    if not matching_employees:
        print("No matching employees found")
    else:
        # Sorting matching employees by pay
        matching_employees.sort(key=lambda x: x[2], reverse=True)
        # Printing header
        print("{:<20} {:<20}".format("Name", "Position"))
        print("-------------------- --------------------")
        # Iterating over matching employees and print name and position
        for employee in matching_employees:
            name, position, pay = employee
            print("{:<20} {:<20}".format(name, position))

def main():
    # Looping until a valid file is entered
    while True:
        # Prompting user to enter a filename
        file_name = input("Enter file name: ")
        try:
            # Attempt to open the file
            with open(file_name, "r") as f:
                # Read all lines from the file except the header
                file_data = f.readlines()[1:]
                # Create a list of employees from the file data
                employee_list = [tuple(line.strip().split(",")) for line in file_data]
                # Exit the loop if the file was successfully read
                break
        except FileNotFoundError:
            # Print an error message if the file was not found
            print("File not found, please try again")
        # Print all employees
    print("Employees:")
    for employee in employee_list:
        print(employee)
    # Loop continues until user quits
    while True:
        # Prompting user to enter pay range
        min_pay = int(input("Enter minimum pay: "))
        max_pay = int(input("Enter maximum pay: "))
        # Displaying employees within pay range
        display_employee_by_pay_range(employee_list, min_pay, max_pay)
        # Prompting user to quit or continue
        choice = input("Enter 'q' to quit, or any other key to continue: ")
        if choice == "q":
            break
# Calling main function if script is run directly
if __name__ == "__main__":
    main()

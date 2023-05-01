from datetime import date
# Getting the user's date of birth
date_of_birth=input("Enter your date of birth in the following format month/day/year: ")
# Convert the date string to a date_of_birth object and handle invalid input
while True:
    try:
        month, day, year=map(int, date_of_birth.split("/"))
        date_of_birth=date(year,month,day)
        break
    except ValueError:
        print("The date format is invalid.Please enter the date in a correct format that is month/day/year")
# Calculating the user's current age
current_day=date.today()
current_age=current_day.year - date_of_birth.year -((current_day.month,current_day.day)<(date_of_birth.month,date_of_birth.day))
# Printing the user's age and date of birth
print("You are",current_age,"years old & your Date of Birth is",date_of_birth.strftime("%d/%m/%Y"))

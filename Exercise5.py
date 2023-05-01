# Importing the numpy library and assigning it the alias "np"
import numpy as np

# Defining a named dtype for the student array, which specifies the data type and field names
student_dtype = np.dtype([('id', int), ('exam_score', int), ('coursework_score', int), ('overall_score', int), ('grade', 'U2')])

# Prompting the user for the name of the marks file
filename = input("Enter the name of the marks file: ")

# Opening the file and reading the first line to get the number of students and the coursework weighting
with open(filename) as f:
    line = f.readline().split()
    num_students = int(line[0]) # Extract the number of students from the first line
    coursework_weight = float(line[1]) / 100 # Extract the coursework weighting from the first line and convert to a float

# Creating a numpy array to hold the student data, with the number of rows determined by the number of students in the file
# adding 4 columns for the ID, exam score, coursework score, and overall score
students = np.zeros((num_students, 4))

# Fill in the first column of the array with the student IDs from the file
with open(filename) as f:
    next(f) # Skip the first line of the file
    for i, line in enumerate(f):
        students[i, 0] = int(line.split()[0]) # Extracting the ID from each line and add it to the first column of the corresponding row

# Filling in the exam and coursework scores for each student and calculate the overall score using the given coursework weighting
students[:, 1] = np.loadtxt(filename, skiprows=1, usecols=1) # Load the exam scores from the file and add them to the second column of the array
students[:, 2] = np.loadtxt(filename, skiprows=1, usecols=2) # Load the coursework scores from the file and add them to the third column of the array
students[:, 3] = np.round(students[:, 1] * (1 - coursework_weight) + students[:, 2] * coursework_weight) # Calculate the overall score for each student using the given coursework weighting

# Defining a function to convert a numeric score to a letter grade based on a set of cutoffs
def calculate_grade(score):
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 40:
        return 'D'
    else:
        return 'F'

# Generating a numpy array to hold the student data, with the same data type as the student_dtype defined earlier
# The array is created using a list comprehension that extracts the relevant data from the students array and calculates the grade using the calculate_grade function
student_array = np.array([(int(id), int(exam_score), int(coursework_score), int(overall_score), calculate_grade(overall_score)) for id, exam_score, coursework_score, overall_score in students], dtype=student_dtype)

# Sorting the student array in descending order by overall score and printing the results to a file
sorted_grades = np.sort(student_array, order='overall_score')[::-1] # Sort the array by the 'overall_score' field in descending order and store the result in a new array
with open('sorted_grades.txt', 'w') as f:
    print(sorted_grades, file=f) # printing the sorted array to a file

# Counting the number of students with each grade and the number of failures
n_a = np.count_nonzero(student_array['grade'] == 'A')
n_b = np.count_nonzero(student_array['grade'] == 'B')
n_c = np.count_nonzero(student_array['grade'] == 'C')
n_d = np.count_nonzero(student_array['grade'] == 'D')
n_f = np.count_nonzero(student_array['grade'] == 'F')

# printing the results to the console
print(f"Number of students with an A grade: {n_a}")
print(f"Number of students with a B grade: {n_b}")
print(f"Number of students with a C grade: {n_c}")
print(f"Number of students with a D grade: {n_d}")
print(f"Number of students who failed: {n_f}")
print("IDs of students who failed:")

# Looping over rows of the student array where the grade is 'F'
for id, grade in student_array[student_array['grade'] == 'F'][['id', 'grade']]:
    # Printing the ID and grade of each failing student
    print(id, grade)

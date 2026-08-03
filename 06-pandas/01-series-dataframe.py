import pandas as pd


student_data = {
    "name": ["An", "Binh", "Chi", "Dung", "Hoa"],
    "math": [8.0, 6.0, 9.5, 4.0, 7.5],
    "english": [7.0, 5.5, 9.0, 5.0, 8.0],
    "science": [9.0, 7.0, 8.5, 4.5, 7.0],
}

# Create a DataFrame from the dictionary
students = pd.DataFrame(student_data)

# 1. Display the entire DataFrame
print("Student DataFrame:")
print(students)

# 2. Display general information
print("\nType:", type(students))
print("Shape:", students.shape)
print("Columns:", students.columns.tolist())

# 3. Display the first five rows
print("\nFirst five rows:")
print(students.head())

# 4. Display DataFrame information
print("\nDataFrame information:")
students.info()

# 5. Display descriptive statistics for numeric columns
print("\nDescriptive statistics:")
print(students.describe())

# 6. Create an average column
score_columns = ["math", "english", "science"]

students["average"] = students[score_columns].mean(axis=1).round(2)

print("\nDataFrame with average column:")
print(students)

# 7. Display names and averages
print("\nStudent names and averages:")
print(students[["name", "average"]])

# 8. Filter passed students
passed_students = students[students["average"] >= 5]

print("\nPassed students:")
print(passed_students[["name", "average"]])

# 9. Filter students whose math score is at least 8
high_math_students = students[students["math"] >= 8]

print("\nStudents with math score at least 8:")
print(high_math_students[["name", "math"]])

# 10. Sort students by average in descending order
sorted_students = students.sort_values(
    by="average",
    ascending=False,
)

print("\nStudents sorted by average:")
print(sorted_students[["name", "average"]])

# 11. Find the student with the highest average
best_student_index = students["average"].idxmax()
best_student = students.loc[best_student_index]

print("\nBest student:")
print("Name:", best_student["name"])
print("Math:", best_student["math"])
print("English:", best_student["english"])
print("Science:", best_student["science"])
print("Average:", best_student["average"])

# 12. Display the final DataFrame
print("\nFinal DataFrame:")
print(students)

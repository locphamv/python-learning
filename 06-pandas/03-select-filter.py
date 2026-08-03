from pathlib import Path

import pandas as pd


# Build the CSV path relative to this file
current_directory = Path(__file__).parent
csv_path = current_directory / "data" / "students.csv"

# Read data from the CSV file
students = pd.read_csv(csv_path)

# Create the average column
score_columns = ["math", "english", "science"]
students["average"] = students[score_columns].mean(axis=1).round(2)

print("Student data:")
print(students)

# 1. Select one column as a Series
names = students["name"]

print("\nNames:")
print(names)
print("Type:", type(names))

# 2. Select multiple columns as a DataFrame
labels = ["name", "math", "average"]
student_summary = students[labels]

print("\nStudent summary:")
print(student_summary)
print("Type:", type(student_summary))

# 3. Select rows by integer position
first_student = students.iloc[0]
first_three_students = students.iloc[:3]
last_student = students.iloc[-1]

print("\nFirst student:")
print(first_student)

print("\nFirst three students:")
print(first_three_students)

print("\nLast student:")
print(last_student)

# 4. Select rows and columns by labels
student_at_index_2 = students.loc[
    2,
    ["name", "average"],
]

print("\nStudent at index 2:")
print(student_at_index_2)

students_at_1_to_3 = students.loc[
    1:3,
    ["name", "math", "average"],
]

print("\nStudents from index 1 to index 3:")
print(students_at_1_to_3)

# 5. Filter using one condition
high_average_students = students[
    students["average"] >= 7
]

low_english_students = students[
    students["english"] < 7
]

print("\nStudents with average at least 7:")
print(high_average_students[["name", "average"]])

print("\nStudents with English score below 7:")
print(low_english_students[["name", "english"]])

# 6. Filter using multiple conditions
strong_math_and_english = students[
    (students["math"] >= 7)
    & (students["english"] >= 7)
]

print("\nStudents strong in math and English:")
print(
    strong_math_and_english[
        ["name", "math", "english"]
    ]
)

strong_math_or_science = students[
    (students["math"] >= 8)
    | (students["science"] >= 8)
]

print("\nStudents strong in math or science:")
print(
    strong_math_or_science[
        ["name", "math", "science"]
    ]
)

# 7. Filter using between
middle_average_students = students[
    students["average"].between(6, 8)
]

print("\nStudents with average between 6 and 8:")
print(
    middle_average_students[
        ["name", "average"]
    ]
)

# 8. Filter using isin
selected_students = students[
    students["name"].isin(
        ["An", "Chi", "Hoa"]
    )
]

print("\nSelected students:")
print(selected_students[["name", "average"]])

# 9. Filter rows and select columns with loc
result = students.loc[
    students["average"] >= 7,
    ["name", "average"],
]

print("\nFiltered result:")
print(result)

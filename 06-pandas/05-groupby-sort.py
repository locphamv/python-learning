from pathlib import Path

import pandas as pd


# Build the CSV path relative to this file
current_directory = Path(__file__).parent
csv_path = current_directory / "data" / "students-groups.csv"

# Read data from the CSV file
students = pd.read_csv(csv_path)

score_columns = ["math", "english", "science"]

# Create the average column
students["average"] = (
    students[score_columns]
    .mean(axis=1)
    .round(2)
)

print("Student data:")
print(students)

# 1. Sort students by average
students_sorted_by_average = students.sort_values(
    by="average",
    ascending=False,
)

print("\nStudents sorted by average:")
print(
    students_sorted_by_average[
        ["class_name", "name", "average"]
    ]
)

# 2. Sort students by class and average
students_sorted_by_class = students.sort_values(
    by=["class_name", "average"],
    ascending=[True, False],
)

print("\nStudents sorted by class and average:")
print(
    students_sorted_by_class[
        ["class_name", "name", "average"]
    ]
)

# 3. Count students in each class
student_counts_by_class = (
    students
    .groupby("class_name")
    .size()
)

print("\nStudent count by class:")
print(student_counts_by_class)

# 4. Calculate average score for each class
class_average_scores = (
    students
    .groupby("class_name")["average"]
    .mean()
    .round(2)
)

print("\nClass average scores:")
print(class_average_scores)

# 5. Calculate subject averages by class
subject_averages_by_class = (
    students
    .groupby("class_name")[score_columns]
    .mean()
    .round(2)
)

print("\nSubject averages by class:")
print(subject_averages_by_class)

# 6. Calculate class statistics
class_statistics = (
    students
    .groupby("class_name")["average"]
    .agg(["mean", "max", "min"])
    .round(2)
)

print("\nClass statistics:")
print(class_statistics)

# 7. Calculate detailed statistics
detailed_statistics = (
    students
    .groupby("class_name")
    .agg(
        {
            "math": ["mean", "max"],
            "english": ["mean", "min"],
            "science": ["mean", "max"],
            "average": ["mean"],
        }
    )
    .round(2)
)

print("\nDetailed statistics:")
print(detailed_statistics)

# 8. Find the best student in each class
best_indices_by_class = (
    students
    .groupby("class_name")["average"]
    .idxmax()
)

best_students_by_class = students.loc[
    best_indices_by_class,
    ["class_name", "name", "average"],
]

print("\nBest student in each class:")
print(best_students_by_class)

# 9. Create the status column
students["status"] = "failed"

students.loc[
    students["average"] >= 5,
    "status",
] = "passed"

# 10. Count statuses by class
status_counts = (
    students
    .groupby(["class_name", "status"])
    .size()
)

status_table = status_counts.unstack(fill_value=0)

print("\nStatus table:")
print(status_table)

status_dataframe = (
    status_counts
    .reset_index(name="student_count")
)

print("\nStatus DataFrame:")
print(status_dataframe)

# 11. Convert class averages into a regular DataFrame
class_average_dataframe = (
    class_average_scores
    .reset_index()
    .rename(
        columns={"average": "class_average"}
    )
)

print("\nClass average DataFrame:")
print(class_average_dataframe)
print("Type:", type(class_average_dataframe))

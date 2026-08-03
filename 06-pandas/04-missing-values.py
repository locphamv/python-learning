from pathlib import Path

import pandas as pd


# Build the CSV path relative to this file
current_directory = Path(__file__).parent
csv_path = current_directory / "data" / "students-missing.csv"

# Read data from the CSV file
students = pd.read_csv(csv_path)

print("Original student data:")
print(students)

# 1. Inspect missing values
missing_mask = students.isna()
missing_counts = missing_mask.sum()
total_missing = missing_counts.sum()

print("\nMissing value mask:")
print(missing_mask)

print("\nMissing values by column:")
print(missing_counts)

print("\nTotal missing values:")
print(total_missing)

# 2. Find rows containing missing values
students_with_missing_data = students[
    students.isna().any(axis=1)
]

print("\nStudents with missing data:")
print(students_with_missing_data)

# 3. Find complete rows using dropna
complete_students = students.dropna()

print("\nComplete students:")
print(complete_students)

# 4. Find complete rows using Boolean filtering
students_dropped = students[
    students.notna().all(axis=1)
]

print("\nData after dropping missing rows:")
print(students_dropped)

print("\nOriginal shape:", students.shape)
print("Dropped shape:", students_dropped.shape)

# 5. Fill all missing values with zero
students_filled_zero = students.fillna(0)

print("\nData filled with zero:")
print(students_filled_zero)

print("\nMissing values after filling with zero:")
print(students_filled_zero.isna().sum())

# 6. Fill missing scores with each subject mean
score_columns = ["math", "english", "science"]

subject_means = students[score_columns].mean()

students_filled_mean = students.copy()

students_filled_mean[score_columns] = (
    students_filled_mean[score_columns].fillna(subject_means)
)

print("\nSubject means:")
print(subject_means.round(2))

print("\nStudents after filling missing scores:")
print(students_filled_mean)

# 7. Create average and status columns
students_filled_mean["average"] = (
    students_filled_mean[score_columns]
    .mean(axis=1)
    .round(2)
)

students_filled_mean["status"] = "failed"

students_filled_mean.loc[
    students_filled_mean["average"] >= 5,
    "status",
] = "passed"

print("\nFinal processed data:")
print(students_filled_mean)

# 8. Verify that the original DataFrame was not modified
print("\nOriginal data after processing:")
print(students)

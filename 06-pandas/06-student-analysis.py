from pathlib import Path
import pandas as pd

current_directory = Path(__file__).parent

students_path = current_directory/"data"/"students-groups.csv"
classes_path = current_directory/"data"/"classes.csv"
output_path = current_directory/"data"/"students-processed.csv"

students = pd.read_csv(students_path)
classes = pd.read_csv(classes_path)

print("Student data:")
print(students)

print("Class data:")
print(classes)

# 1. Inspect the data
print(students.shape)
print(students.columns)
print(students.dtypes)
print(students.isna().sum())

# 2 average col
score_columns = ["math", "english", "science"]
students["average"] = students[score_columns].mean(axis=1).round(2)
print(students)

# 3 status col
students["status"] = "failed"
students.loc[students["average"] >= 5, "status"] = "passed"
print(students)

# 4 grade col
students["grade"] = "F"
students.loc[students["average"] >= 5, "grade"] = "C"
students.loc[students["average"] >= 7, "grade"] = "B"
students.loc[students["average"] >= 8.5, "grade"] = "A"
print(students)

# 5 merge class
student_details = students.merge(
    classes,
    on="class_name",
    how="left"
)

print(
    student_details[
        ["name",
         "class_name",
         "teacher",
         "room",
         "average"]
    ]
)

ranking = student_details.sort_values(
    "average",
    ascending=False,
)

ranking = ranking.reset_index(drop=True)
ranking["rank"] = ranking.index + 1
ranking = ranking[
    [
        "rank",
        "name",
        "class_name",
        "average",
        "grade",
    ]
]
print(ranking)

# filter students
passed_students = students[students["status"] == "passed"]
failed_students = students[students["status"] == "failed"]
excellent_students = students[students["average"] >= 8]

print(
    excellent_students[
        ["name", "class_name", "average"]
    ]
)

# find best student
best_student_index = students["average"].idxmax()
best_student = student_details.loc[
    best_student_index
]
print("Name:", best_student["name"])
print("Class:", best_student["class_name"])
print("Teacher:", best_student["teacher"])
print("Average:", best_student["average"])

# find the best student in each class
best_indices_by_class = (
    student_details
    .groupby("class_name")["average"]
    .idxmax()
)

best_students_by_class = student_details.loc[
    best_indices_by_class,
    [
        "class_name",
        "name",
        "average",
    ],
]

print(best_students_by_class)

# 10. stats
class_statistics = (
    student_details
    .groupby("class_name")
    .agg(
        student_count=("name", "size"),
        class_average=("average", "mean"),
        highest_average=("average", "max"),
        lowest_average=("average", "min"),
    )
    .round(2)
    .reset_index()
)

print(class_statistics)

#  status stats
status_table = (
    student_details
    .groupby(
        ["class_name", "status"]
    )
    .size()
    .unstack(fill_value=0)
)
print(status_table)

# 12 turn data into numpy preparing for machine learning

X = student_details[
    ["math", "english", "science"]
].to_numpy()

y = student_details["status"].to_numpy()

print("\nFeature array:")
print(X)
print("Feature shape:", X.shape)

print("\nLabel array:")
print(y)
print("Label shape:", y.shape)

# 13. save processed data to csv
student_details.to_csv(
    output_path,
    index=False,
)
print("\nSaved processed data to:")
print(output_path)

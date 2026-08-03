from pathlib import Path

import numpy as np
import pandas as pd

current_directory = Path(__file__).parent
csv_path = current_directory / "data" / "students.csv"

students = pd.read_csv(csv_path)

print("Student data:")
print(students)

# 1. General info
print("Type:", type(students))
print("Shape:", students.shape)
print("Columns:", students.columns.tolist())

# 2. Create the average column
score_columns = ["math", "english", "science"]
students["average"] = students[score_columns].mean(axis=1).round(2)
print(students)

# 3. create the status column and filter
students["status"] = "Fail"
students.loc[students["average"] >= 5, "status"] = "Pass"
print(students)

# 4 Find the best math student/ dataframe type printing
best_math_index = students["math"].idxmax()
best_math_student = students.loc[[best_math_index]]
print("\nBest math student:")
print(best_math_student)

# 5 best overall stu/ series type printing
best_overall_student = students.loc[students["average"].idxmax()]
print("\nBest overall student:")
print(best_overall_student)

# 6 subject average
print("\nMath average:", round(students["math"].mean(), 2))
print("Englis average:", round(students["english"].mean(), 2))
print("Science average:", round(students["science"].mean(), 2))

# 7 calculate counts and pass rate
is_pass = students["status"] == "Pass"

pass_count = is_pass.sum()
fail_count = (~is_pass).sum()
total_count = len(students)

pass_rate = (pass_count / total_count) * 100

print("\nPass count:", pass_count)
print("Fail count:", fail_count)
print("Pass rate:", round(pass_rate, 2), "%")

# 8 sort students by average
ranked_students= students.sort_values("average", ascending=False)
print(ranked_students)

print("\nFinal DataFrame:")
print(students)

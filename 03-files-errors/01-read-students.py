import csv
from pathlib import Path

file_path = Path(__file__).parent/"data"/"students.csv"
students = []

with open(file_path, mode="r", encoding="utf-8", newline ="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            student = {
                    "name": row["name"],
                    "score": float(row["score"])
            }
            students.append(student)

print("Student names: ")

for student in students:
      print(student["name"])

if students:
    total_score =0

    for student in students:
        total_score += student["score"]

    average_score = total_score / len(students)

    highest_student = students[0]

    for student in students:
        if student["score"] > highest_student["score"]:
             highest_student = student

    passed_students = []
    for student in students:
         if student["score"] >= 5:
              passed_students.append(student)

    print(f"\nAverage score: {average_score:.2f}")
    print(
         f"Highest-scoring sudents: "
         f"{highest_student['name']}-{highest_student['score']}"
    )

    print("\nPassed students: ")

    for student in passed_students:
         print(f"{student['name']} - {student['score']}")
else:
     print("No student data found.")
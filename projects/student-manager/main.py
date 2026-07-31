students = {
    "SV001": {"name": "An", "score": 8.5},
    "SV002": {"name": "Binh", "score": 6.0}
}

def add_student(students, student_id, name, score):
    if student_id in students:
        return f"Student ID {student_id} already exist."

    if (
        isinstance(score, bool)
        or not isinstance(score, (int, float))
        or not 0 <= score <= 10
    ):
        return "Score must be a number between 0 and 10."

    students[student_id] = {
        "name": name,
        "score": float(score)
    }

    return f"Student {student_id} was added successfully."

def remove_student(students, student_id):
    if student_id not in students:
        return f"Student with ID {student_id} was not found."

    removed_student = students.pop(student_id)

    return (
        f"Student {student_id} - {removed_student['name']}"
        "was removed successfully."
    )

def find_student(students, student_id):
    student = students.get(student_id)

    if student_id not in students:
        return f"Student with ID {student_id} was not found."

    return {
        "student_id": student_id,
        "name": student["name"],
        "score": student["score"],
    }

def show_students(students):
    if not students:
        print("The student list is empty.")
        return

    sorted_students = sorted(
        students.items(),
        key= lambda item: item[1]["score"],
        reverse = True
    )

    print("\nSTUDENT LIST")
    print ("-"* 42)

    for student_id, student_info in sorted_students:
        print(
            f"{student_id: <12}"
            f"{student_info['name']: <20}"
            f"{student_info['score']: >10.1f}"
        )

    print("_" * 42)

def calculate_average(students):
    if not students:
        return 0.0

    total_score = sum(
        student["score"] for student in students.values()
    )

    return total_score / len(students)

if __name__ == "__main__":
    print(add_student(students, "SV003", "Chi", 9.0))
    print(add_student(students, "SV001", "Dung", 7.5))
    print(add_student(students, "SV004", "Hoa", 12))

print("\nSearch results: ")
print(find_student(students, "SC002"))
print(find_student(students, "SV999"))

show_students(students)

average_score = calculate_average(students)
print(f"\nAverage score: {average_score: .2f}")

print(remove_student(students, "SV002"))
print(remove_student(students, "SV999"))

show_students(students)
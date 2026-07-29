course_name = input("Course name: ")
total_lessons = int(input("Total lessons: "))
completed_lessons = int(input("Completed lessons: "))

if total_lessons <= 0:
    print("Total lessons must be greater than 0.")
elif completed_lessons < 0:
    print("Completed lessons cannot be negative.")
elif completed_lessons > total_lessons:
    print("Completed lessons cannot exceed total lessons." )
else:
    progress = completed_lessons / total_lessons * 100

    print(f"Course: {course_name}")
    print(f"Completed: {completed_lessons}/{total_lessons}")
    print(f"Progress: {progress:.1f}%")

    if progress==100:
        print("You have completed the course!")
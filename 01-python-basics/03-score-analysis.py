scores =[7.5, 8.0, 4.5, 9.0, 6.5, 3.5, 8.5]

student_count = len(scores)
highest_score = max(scores)
lowest_score = min(scores)
average_score = sum(scores) / student_count
sorted_scores = sorted(scores, reverse = True)

passed_count = 0
failed_count = 0

for score in scores:
    if score > 5:
        passed_count += 1
    else:
        failed_count += 1

print(f"Number of students: {student_count}")
print(f"Highest score: {highest_score}")
print(f"lowest score:  {lowest_score}")
print(f"Average score: {average_score: .2f}")
print(f"Number of students who passed: {passed_count}")
print(f"Number of students who failed: {failed_count}")
print(f"From highest to lowest: {sorted_scores}")


import numpy as np


names = np.array(["An", "Binh", "Chi", "Dung", "Hoa"])

scores = np.array(
    [
        [8.0, 7.0, 9.0],
        [6.0, 5.5, 7.0],
        [9.5, 9.0, 8.5],
        [4.0, 5.0, 4.5],
        [7.5, 8.0, 7.0],
    ]
)

print("Names:")
print(names)

print("\nScores:")
print(scores)

# 1. Average of each student
student_averages = scores.mean(axis=1)

print("\nStudent averages:")
print(np.round(student_averages, 2))

# 2. Average of each subject
subject_averages = scores.mean(axis=0)

print("\nSubject averages:")
print(np.round(subject_averages, 2))

# 3. Best student
best_student_index = student_averages.argmax()
best_student_name = names[best_student_index]
best_student_average = student_averages[best_student_index]
best_student_scores = scores[best_student_index]

print("\nBest student:")
print("Name:", best_student_name)
print("Scores:", best_student_scores)
print("Average:", round(best_student_average, 2))

# 4. Passed students
passed_mask = student_averages >= 5

passed_names = names[passed_mask]
passed_scores = scores[passed_mask]
passed_averages = student_averages[passed_mask]

print("\nPassed students:")
print("Names:", passed_names)
print("Scores:")
print(passed_scores)
print("Averages:", np.round(passed_averages, 2))

# 5. Sort students by average in descending order
sorted_indices = np.argsort(student_averages)[::-1]

sorted_names = names[sorted_indices]
sorted_scores = scores[sorted_indices]
sorted_averages = student_averages[sorted_indices]

print("\nStudents sorted by average:")
print("Names:", sorted_names)
print("Scores:")
print(sorted_scores)
print("Averages:", np.round(sorted_averages, 2))

# 6. Min-max normalization by subject
subject_minimums = scores.min(axis=0)
subject_maximums = scores.max(axis=0)

score_ranges = subject_maximums - subject_minimums
safe_ranges = np.where(score_ranges == 0, 1, score_ranges)

normalized_scores = (scores - subject_minimums) / safe_ranges

print("\nMinimum score of each subject:")
print(subject_minimums)

print("Maximum score of each subject:")
print(subject_maximums)

print("Normalized scores:")
print(np.round(normalized_scores, 2))

# 7. Split train and test using shared indices
rng = np.random.default_rng(42)
indices = rng.permutation(names.size)

test_ratio = 0.2
test_size = int(names.size * test_ratio)
test_size = max(1, test_size)
test_size = min(test_size, names.size - 1)

test_indices = indices[-test_size:]
train_indices = indices[:-test_size]

names_train = names[train_indices]
scores_train = scores[train_indices]

names_test = names[test_indices]
scores_test = scores[test_indices]

print("\nTrain set:")
print("Names:", names_train)
print("Scores:")
print(scores_train)

print("\nTest set:")
print("Names:", names_test)
print("Scores:")
print(scores_test)

# 8. Check that original data was not modified
print("\nOriginal data after processing:")
print("Names:", names)
print("Scores:")
print(scores)

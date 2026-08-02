import numpy as np

scores = np.array(
    [
        [8.0, 7.5, 9.0],
        [6.0, 6.5, 7.0],
        [9.0, 8.5, 9.5],
    ]
)

bonus = np.array([0.5, 1.0, 1.0])

print("Original scores:")
print(scores)

print("\nScores shape:", scores.shape)
print("Bonus shape:", bonus.shape)

# 1
updated_scores = scores + bonus

print("\nScores after adding bonus:")
print(updated_scores)

# 2
clipped_scores = np.clip(updated_scores, 0, 10)

print("\nScores after clipping:")
print(clipped_scores)

# 3
student_averages = clipped_scores.mean(axis=1)

print("\nStudent averages:")
print(np.round(student_averages, 2))

# 4
subject_averages = clipped_scores.mean(axis=0)
print("\nSubject averages:")
print(np.round(subject_averages, 2))

# 5
print("\nOriginal scores after operations:")
print(scores)


# 6
subject_weights = np.array([0.3, 0.3, 0.4])

weighted_scores = clipped_scores * subject_weights
final_scores = weighted_scores.sum(axis=1)

print("\nSubject weights:", subject_weights)
print("Weighted scores: ")
print(weighted_scores)

print("\nFinal weighted scores:")
print(np.round(final_scores, 2))


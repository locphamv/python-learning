import numpy as np

study_hours = np.array([
    1, 2, 3, 4, 5, 6, 7
])

scores = np.array([
    4.0, 5.0, 5.5, 7.0, 7.5, 8.5, 9.5
])

correlation_matrix = np.corrcoef(
    study_hours,
    scores,
)

correlation = correlation_matrix[0, 1]

print("Study hours correlation matrix:")
print(correlation_matrix)
print("Correlation:", correlation)
absences = np.array([
    0, 1, 2, 3, 4, 5, 6
])

exam_scores = np.array([
    9.5, 9.0, 8.5, 7.0, 6.5, 5.0, 4.0
])

correlation_matrix_2 = np.corrcoef(
    absences,
    exam_scores
)

correlation_2 = correlation_matrix_2[0, 1]


print("\nAbsences correlation matrix:")
print(correlation_matrix_2)
print("Correlation:", correlation_2)

# Dataset 1 has a strong positive correlation.
# Dataset 2 has a strong negative correlation.

import numpy as np

study_hours = np.array([
    1, 2, 3, 4, 5
])

absences = np.array([
    5, 4, 3, 2, 1
])

previous_scores = np.array([
    4.0, 5.0, 6.0, 7.0, 8.0
])

final_scores = np.array([
    4.5, 5.5, 6.5, 7.5, 9.0
])

X = np.column_stack([
    study_hours,
    absences,
    previous_scores,
])

y = final_scores

print(X)
print("X shape:", X.shape)
print(y)
print("y shape:", y.shape)

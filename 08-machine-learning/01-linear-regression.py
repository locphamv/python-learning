import numpy as np
from sklearn.linear_model import LinearRegression

study_hours = np.array([
    1, 2, 3, 4, 5, 6, 7
])

scores = np.array([
    4.0, 5.0, 5.5, 7.0, 7.5, 8.5, 9.5
])

X = study_hours.reshape(-1, 1)
y = scores
print("X shape:", X.shape)
print("y shape:", y.shape)

model = LinearRegression()
model.fit(X, y)

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

new_student = np.array([
    [8]
])

predicted_score = model.predict(
    new_student
)

print(
    "Predicted score:",
    predicted_score
)

new_students = np.array([
    [2.5],
    [5.5],
    [8],
])

predicted_scores = model.predict(
    new_students
)

print(
    "Predicted scores:",
    predicted_scores
)

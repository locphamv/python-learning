import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Create dataset
study_hours = np.array([
    1.0, 1.5, 2.0, 2.5,
    3.0, 3.5, 4.0, 4.5,
    5.0, 5.5, 6.0, 6.5,
    7.0, 7.5, 8.0, 8.5,
])

passes = np.array([
    0, 0, 0, 0,
    0, 0, 0, 1,
    0, 1, 1, 1,
    1, 1, 1, 1,
])

X = study_hours.reshape(-1, 1)
y = passes


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)


# Scale the data
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Create and train the model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)


# Make predictions
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)


# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
matrix = confusion_matrix(y_test, y_pred)


# Predict a new student
new_student = np.array([[5.2]])
new_student_scaled = scaler.transform(new_student)

new_prediction = model.predict(new_student_scaled)[0]
new_probability = model.predict_proba(new_student_scaled)[0, 1]


# Print results
print("Actual:", y_test)
print("Predicted:", y_pred)

print("\nPass probabilities:")
print(y_proba[:, 1])

print("\nConfusion matrix:")
print(matrix)

print("\nAccuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)

print("\nNew student prediction:", new_prediction)
print("Pass probability:", round(new_probability, 3))

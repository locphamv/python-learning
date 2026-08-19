import numpy as np

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text


study_hours = np.array([
    1.0, 1.5, 2.0, 2.5,
    3.0, 3.5, 4.0, 4.5,
    5.0, 5.5, 6.0, 6.5,
    7.0, 7.5, 8.0, 8.5,
])

absences = np.array([
    6, 6, 5, 5,
    4, 4, 3, 3,
    3, 2, 2, 1,
    1, 1, 0, 0,
])

previous_scores = np.array([
    3.5, 4.0, 4.2, 4.5,
    5.0, 5.2, 5.5, 6.0,
    5.8, 6.5, 7.0, 7.2,
    7.8, 8.0, 8.5, 9.0,
])

passed = np.array([
    0, 0, 0, 0,
    0, 0, 0, 1,
    0, 1, 1, 1,
    1, 1, 1, 1,
])


# Combine features into one feature matrix
X = np.column_stack([
    study_hours,
    absences,
    previous_scores,
])

y = passed


# Split data while keeping class proportions
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)


# Limit tree depth to reduce overfitting
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42,
)

model.fit(X_train, y_train)


# Predict train and test data
y_train_pred = model.predict(X_train)
y_pred = model.predict(X_test)


# Evaluation metrics
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

matrix = confusion_matrix(y_test, y_pred)


print("Actual:", y_test)
print("Predicted:", y_pred)

print("\nConfusion matrix:")
print(matrix)

print("\nTraining accuracy:", train_accuracy, 3)
print("Test accuracy:", test_accuracy, 3)
print("Precision:", precision, 3)
print("Recall:", recall, 3)
print("F1:", f1, 3)


# Show learned decision rules
feature_names = [
    "study_hours",
    "absences",
    "previous_score",
]

tree_rules = export_text(
    model,
    feature_names=feature_names,
)

print("\nTree rules:")
print(tree_rules)


# Predict a new student
new_student = np.array([
    [6.0, 1, 7.5]
])

prediction = model.predict(new_student)[0]

print("New student prediction:", prediction)


# Show how important each feature is to the tree
print("\nFeature importance:")

for feature, importance in zip(
    feature_names,
    model.feature_importances_,
):
    print(
        feature,
        round(importance, 3),
    )

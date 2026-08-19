import numpy as np

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier


X = np.array([
    [1.0, 6, 3.5],
    [1.5, 6, 4.0],
    [2.0, 5, 4.2],
    [2.5, 5, 4.5],
    [3.0, 4, 5.0],
    [3.5, 4, 5.2],
    [4.0, 3, 5.5],
    [4.5, 3, 6.0],
    [5.0, 3, 5.8],
    [5.5, 2, 6.5],
    [6.0, 2, 7.0],
    [6.5, 1, 7.2],
    [7.0, 1, 7.8],
    [7.5, 1, 8.0],
    [8.0, 0, 8.5],
    [8.5, 0, 9.0],
    [2.2, 4, 4.8],
    [3.8, 2, 6.1],
    [5.2, 4, 6.0],
    [6.8, 3, 7.0],
    [7.2, 2, 7.5],
    [4.2, 5, 5.1],
    [5.8, 1, 7.1],
    [8.2, 2, 8.4],
])

y = np.array([
    0, 0, 0, 0,
    0, 0, 0, 1,
    0, 1, 1, 1,
    1, 1, 1, 1,
    0, 0, 1, 1,
    1, 0, 1, 1,
])


# Part 1: Evaluate one model using 5-fold cross-validation
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42,
)

scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="accuracy",
)

print("Cross-validation scores:")
print(scores)

print("Mean accuracy:", round(scores.mean(), 3))
print("Standard deviation:", round(scores.std(), 3))


# Part 2: Compare different max_depth values
depths = [
    1,
    2,
    3,
    4,
    5,
    None,
]

print("\nDepth comparison:")

for depth in depths:
    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42,
    )

    scores = cross_val_score(
        model,
        X,
        y,
        cv=5,
        scoring="accuracy",
    )

    print(
        "Max depth:",
        depth,
        "Mean accuracy:",
        round(scores.mean(), 3),
        "Std:",
        round(scores.std(), 3),
    )

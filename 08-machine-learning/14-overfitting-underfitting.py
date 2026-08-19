import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
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


# Split data while keeping the same class ratio in train and test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y,
)


# Test different maximum tree depths
depths = [
    1,
    2,
    3,
    4,
    5,
    None,
]


for depth in depths:
    # max_depth=None means the tree has no explicit depth limit
    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42,
    )

    model.fit(
        X_train,
        y_train,
    )

    # Predict both training and testing data
    # to compare how well the model fits and generalizes
    train_pred = model.predict(
        X_train
    )

    test_pred = model.predict(
        X_test
    )

    train_accuracy = accuracy_score(
        y_train,
        train_pred,
    )

    test_accuracy = accuracy_score(
        y_test,
        test_pred,
    )

    print(
        "Max depth:",
        depth,
        "Train accuracy:",
        round(train_accuracy, 3),
        "Test accuracy:",
        round(test_accuracy, 3),
    )

    # Show the depth the tree actually used
    print(
        "Actual tree depth:",
        model.get_depth(),
    )

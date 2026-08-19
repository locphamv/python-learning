import numpy as np

from sklearn.model_selection import GridSearchCV, train_test_split
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


# Keep the test set separate so it is only used for final evaluation.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)


model = DecisionTreeClassifier(
    random_state=42
)


# Hyperparameter values that GridSearchCV will try.
param_grid = {
    "max_depth": [
        1,
        2,
        3,
        4,
        5,
        None,
    ]
}


# Try every max_depth using 5-fold cross-validation.
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
)


# Grid search must only use the training data.
grid_search.fit(
    X_train,
    y_train,
)


print(
    "Best parameters:",
    grid_search.best_params_,
)

print(
    "Best CV score:",
    grid_search.best_score_,
)


# With refit=True by default, this model has already been fit on all training data.
best_model = grid_search.best_estimator_


test_accuracy = best_model.score(
    X_test,
    y_test,
)

print(
    "Final test accuracy:",
    test_accuracy,
)


# cv_results_ contains the score for every tested configuration.
results = grid_search.cv_results_

for params, mean_score in zip(
    results["params"],
    results["mean_test_score"],
):
    print(
        params,
        round(mean_score, 3),
    )

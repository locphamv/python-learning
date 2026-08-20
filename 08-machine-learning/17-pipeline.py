import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


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
])


y = np.array([
    0, 0, 0, 0,
    0, 0, 0, 1,
    0, 1, 1, 1,
    1, 1, 1, 1,
])


# Keep test data separate for final evaluation.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)


# Pipeline keeps preprocessing and model together.
pipeline = Pipeline([
    (
        "scaler",
        StandardScaler(),
    ),
    (
        "model",
        LogisticRegression(),
    ),
])


# Pipeline automatically fits the scaler first, then the model.
pipeline.fit(
    X_train,
    y_train,
)


# X_test is automatically transformed by the fitted scaler before prediction.
y_pred = pipeline.predict(
    X_test
)


accuracy = accuracy_score(
    y_test,
    y_pred,
)

print(
    "Accuracy:",
    accuracy,
)

print(
    "Pipeline score:",
    pipeline.score(
        X_test,
        y_test,
    ),
)


new_student = np.array([
    [6.0, 1, 7.5]
])


# No manual scaling is needed for new data.
prediction = pipeline.predict(
    new_student
)

print(
    "Prediction:",
    prediction[0],
)


probabilities = pipeline.predict_proba(
    new_student
)

print(
    "Pass probability:",
    probabilities[0, 1],
)


# Access fitted components inside the pipeline.
scaler = pipeline.named_steps[
    "scaler"
]

model = pipeline.named_steps[
    "model"
]

print(
    "Scaler mean:",
    scaler.mean_,
)

print(
    "Coefficients:",
    model.coef_,
)


# Pipeline parameters use: step_name__parameter_name.
param_grid = {
    "model__C": [
        0.1,
        1.0,
        10.0,
    ],
}


grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
)


# GridSearchCV fits the whole pipeline separately inside each CV fold.
# This prevents the scaler from seeing validation data during training.
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


# best_estimator_ is the best pipeline, including both scaler and model.
best_pipeline = grid_search.best_estimator_


final_test_accuracy = best_pipeline.score(
    X_test,
    y_test,
)

print(
    "Final test accuracy:",
    final_test_accuracy,
)

from pathlib import Path

import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
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


# Train once before saving.
pipeline.fit(
    X,
    y,
)


current_directory = Path(__file__).parent

models_directory = (
    current_directory / "models"
)

models_directory.mkdir(
    exist_ok=True
)

model_path = (
    models_directory
    / "student-pass-pipeline.joblib"
)


test_student = np.array([
    [6.0, 1, 7.5]
])

prediction_before_save = pipeline.predict(
    test_student
)

print(
    "Before save:",
    prediction_before_save[0],
)


# Save the fitted pipeline, including scaler and model state.
joblib.dump(
    pipeline,
    model_path,
)

print(
    "Model saved to:",
    model_path,
)

from pathlib import Path

import joblib
import numpy as np


current_directory = Path(__file__).parent

model_path = (
    current_directory
    / "models"
    / "student-pass-pipeline.joblib"
)


# Load the already-trained pipeline.
pipeline = joblib.load(
    model_path
)


new_student = np.array([
    [6.0, 1, 7.5]
])


prediction = pipeline.predict(
    new_student
)

probabilities = pipeline.predict_proba(
    new_student
)


print(
    "Prediction:",
    prediction[0],
)

print(
    "Pass probability:",
    round(
        probabilities[0, 1],
        3,
    ),
)

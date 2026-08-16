import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    r2_score,
    root_mean_squared_error,
)
from sklearn.model_selection import train_test_split

study_hours = np.array([
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    3, 5, 7, 9, 4,
])

absences = np.array([
    6, 5, 5, 4, 3,
    3, 2, 2, 1, 0,
    6, 4, 3, 1, 5,
])

previous_scores = np.array([
    4.0, 4.5, 5.0, 5.5, 6.0,
    6.5, 7.0, 7.5, 8.0, 8.5,
    5.0, 6.0, 7.0, 8.0, 5.5,
])

final_scores = np.array([
    3.8, 4.5, 4.8, 5.5, 6.2,
    6.8, 7.3, 7.8, 8.5, 9.2,
    4.6, 6.1, 7.2, 8.7, 5.2,
])

X = np.column_stack([
    study_hours,
    absences,
    previous_scores,
])

y = final_scores


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

for actual, predicted in zip(
    y_test,
    y_pred,
):
    print(
        "Actual:",
        actual,
        "Predicted:",
        predicted,
    )

mae = mean_absolute_error(
    y_test,
    y_pred,
)

rmse = root_mean_squared_error(
    y_test,
    y_pred,
)

r2 = r2_score(
    y_test,
    y_pred,
)


print("MAE:", round(mae, 3))
print("RMSE:", round(rmse, 3))
print("R2:", round(r2, 3))

new_student = np.array([
    [8, 1, 8.0]
])

new_pred = model.predict(new_student)
print("New student's final score:", round(new_pred[0], 2),)

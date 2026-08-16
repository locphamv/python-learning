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
    11, 12, 13, 14, 15,
])

scores = np.array([
    3.0, 3.8, 4.5, 5.0, 5.8,
    6.2, 6.8, 7.3, 7.7, 8.2,
    8.5, 8.9, 9.1, 9.4, 9.6,
])

X = study_hours.reshape(-1, 1)
y = scores

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

model = LinearRegression()

model.fit(
    X_train,
    y_train,
)

y_pred = model.predict(X_test)

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

for actual, predicted in zip(
    y_test,
    y_pred,
):
    print(
        "Actual:",
        actual,
        "Predicted:",
        round(predicted, 2),
    )




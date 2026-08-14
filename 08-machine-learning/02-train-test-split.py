import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

study_hours = np.array([
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
])

scores = np.array([
    3.5, 4.5, 5.0, 5.5, 6.0,
    7.0, 7.5, 8.0, 9.0, 9.5,
])

X = study_hours.reshape(-1, 1)
y = scores

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

print("X train shape:")
print(X_train.shape)

print("X test shape:")
print(X_test.shape)

print("y train shape:")
print(y_train.shape)

print("y test shape:")
print(y_test.shape)


model = LinearRegression()
model.fit(
    X_train,
    y_train,
)

y_pred = model.predict(X_test)

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

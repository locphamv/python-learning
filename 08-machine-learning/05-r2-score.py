import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


study_hours = np.array([
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
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


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

r2 = r2_score(
    y_test,
    y_pred,
)
model_r2 = model.score(
    X_test,
    y_test
)


print("R2 score:", r2)
print("model.score:", model_r2)

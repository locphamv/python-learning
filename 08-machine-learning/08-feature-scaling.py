import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = np.array([
    [18, 20000],
    [20, 25000],
    [22, 30000],
    [25, 40000],
    [28, 50000],
    [30, 60000],
    [35, 75000],
    [40, 90000],
])

y = np.array([
    0, 0, 0, 0,
    1, 1, 1, 1,
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)

print("Original X train:")
print(X_train)

print("\nScaled X train:")
print(X_train_scaled)

print("Mean:", scaler.mean_)
print("Scale:", scaler.scale_)

new_person = np.array([
    [27, 45000]
])
new_person_scaled = scaler.transform(
    new_person
)
print("\nOriginal new person:")
print(new_person)

print("\nScaled new person:")
print(new_person_scaled)

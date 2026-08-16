import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Feature matrix: [age, income]
X = np.array([
    [18, 20000],
    [20, 25000],
    [22, 30000],
    [24, 35000],
    [26, 40000],
    [28, 50000],
    [30, 60000],
    [32, 65000],
    [35, 75000],
    [38, 85000],
    [40, 90000],
    [45, 100000],
])

# Target labels
y = np.array([
    0, 0, 0, 0,
    0, 0, 1, 1,
    1, 1, 1, 1,
])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

# Create a standard scaler
scaler = StandardScaler()


# Fit the scaler on the training data and transform it
X_train_scaled = scaler.fit_transform(
    X_train
)

# Transform the test data using the same scaler
X_test_scaled = scaler.transform(
    X_test
)

# Create a KNN classifier using 3 nearest neighbors
model = KNeighborsClassifier(
    n_neighbors=3
)

# Train the model
model.fit(
    X_train_scaled,
    y_train,
)

# Predict labels for the test set
y_pred = model.predict(
    X_test_scaled
)

# Compare actual and predicted labels
print("Actual:", y_test)
print("Predicted:", y_pred)

# Calculate model accuracy
accuracy = accuracy_score(
    y_test,
    y_pred,
)

print("Accuracy:", accuracy)

# Create a new person's data: [age, income]
new_person = np.array([
    [31, 62000]
])

# Scale the new data using the previously fitted scaler
new_person_scaled = scaler.transform(new_person)

# Predict the class of the new person
prediction = model.predict(new_person_scaled)
print(
    "New person predictions:",
    prediction[0],
)

# Find the 3 nearest neighbors of the new person
distances, indices = model.kneighbors(
    new_person_scaled
)

# Print the distances to the nearest neighbors
print(
    "Neighbor distances:",
    distances,
)

# Print the indices of the nearest neighbors in X_train
print(
    "Neighbor indices:",
    indices,
)

# Print the original feature values of the nearest neighbors
print(X_train[indices[0]])

# Print the labels of the nearest neighbors
print(y_train[indices[0]])

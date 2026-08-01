import random

features = [
    [20, 5],
    [25, 7],
    [30, 8],
    [35, 10],
    [40, 12],
    [45, 15],
    [50, 18],
    [55, 20],
    [60, 22],
    [65, 25],
]

labels = [
    "low",
    "low",
    "low",
    "medium",
    "medium",
    "medium",
    "high",
    "high",
    "high",
    "high",
]

def split_features_labels(features, labels, test_ratio, seed=None):
    if len(features) != len(labels):
        raise ValueError("Features and labels must have the same length")

    if not 0 < test_ratio < 1:
        raise ValueError("test_radio must be between 0 and 1")

    if len(features) < 2:
        raise ValueError("At least 2 items to split train and test")

    paired_data = list(zip(features, labels))

    random_generator = random.Random(seed)
    random_generator.shuffle(paired_data)

    test_size = int(len(paired_data) * test_ratio)
    test_size = max(1, test_size)
    test_size = min(test_size, len(paired_data)- 1)

    test_pairs = paired_data[: test_size]
    train_pairs = paired_data[test_size: ]

    x_train = [pair[0] for pair in train_pairs]
    y_train = [pair[1] for pair in train_pairs]

    x_test = [pair[0] for pair in test_pairs]
    y_test = [pair[1] for pair in test_pairs]

    return x_train, x_test, y_train, y_test

x_train, x_test, y_train, y_test = split_features_labels(
    features,
    labels,
    test_ratio= 0.2,
    seed= 42,
)

print("X train: ", x_train)
print("X test: ", x_test)
print("Y train: ", y_train)
print("Y test: ", y_test)

print("origin data: ")
print("Features: ", features)
print("Labels: ", labels)

import numpy as np


def normalize(values):
    values = np.asarray(values, dtype=float)

    if values.size == 0:
        return np.array([], dtype=float)

    minimum_value = values.min()
    maximum_value = values.max()

    if minimum_value == maximum_value:
        return np.zeros_like(values)

    normalized_values = (
        (values - minimum_value)
        / (maximum_value - minimum_value)
    )

    return normalized_values


values = np.array([10, 20, 30, 40, 50])

result = normalize(values)

print("Original values:", values)
print("Normalized values:", result)

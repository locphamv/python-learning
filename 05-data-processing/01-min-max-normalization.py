
def min_max_normalize(values):
    if not values:
        return []

    min_value = min(values)
    max_value = max(values)

    if min_value == max_value:
        return [0.0] * len(values)

    return [
        (value - min_value) / (max_value - min_value)
        for value in values
    ]

values = [10, 20, 30, 40, 50]
print(min_max_normalize(values))


values = []
print(min_max_normalize(values))

values = [5, 5, 5, 5]
print(min_max_normalize(values))

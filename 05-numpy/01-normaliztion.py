values = [10,20,30,40,50]

def normalize(values):
    if not values:
        return []

    minimum_value = min(values)
    maximum_value = max(values)

    if minimum_value == maximum_value:
        return [0.0 for value in values]
    normalized_value = []

    for value in values:
        tmp = (
            (value - minimum_value) / (maximum_value - minimum_value)
        )
        normalized_value.append(tmp)
    return normalized_value

result = normalize(values)
print(result)
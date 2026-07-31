raw_values = ["10", "20", "", "abc", "30.5", "-5", "40"]

def clean_numeric_data(values):
    cleaned_values = []

    for value in values:
        if value == "":
            continue

        try:
            number = float(value)

            if number < 0:
                continue
            cleaned_values.append(number)

        except ValueError:
            continue
    return cleaned_values

results = clean_numeric_data(raw_values)


print(results)
print (raw_values)
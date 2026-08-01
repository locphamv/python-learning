import numpy as np

values = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print("Original array:", values)

first_value = values[0]
print("First value:", first_value)

last_value = values[-1]
print("Last value:", last_value)

first_three = values[:3]
print("First three values:", first_three)

last_three = values[-3:]
print("Last three values:", last_three)

values_from_index_2_to_4 = values[2:5]
print("Values from index 2 to 4:", values_from_index_2_to_4)

values_including_index_5 = values[2:6]
print("Values from index 2 to 5", values_including_index_5)

even_index_values = values[::2]
print("Values at even indexes:", even_index_values)

# NumPy can perform Boolean filtering directly
greater_than_40 = values[values > 40]
print("Values greater than 40:", greater_than_40)

between_30_and_60 = values[(values >= 30) & (values <= 60)]
print("Values between 30 and 60:", between_30_and_60)

modified_values = values.copy()
modified_values[modified_values < 30] = 0

print("Modified array:", modified_values)
print("Original array after modification:", values)


divisible_by_20 = values[values % 20 == 0]
print("Divisible by 20:", divisible_by_20)


outside_range = values[(values < 30) | (values > 60)]
print("Outside 30-60:", outside_range)


reversed_values = values[::-1]
print("Reversed:", reversed_values)


replaced_values = values.copy()
mask = (replaced_values >= 30) & (replaced_values <= 50)
replaced_values[mask] = -1

print("Replaced values:", replaced_values)


import numpy as np

scores = [7.5, 8.0, 4.5, 9.0, 6.5, 3.5, 8.5]

scores_array = np.array(scores)

print("Scores: ", scores_array)
print("Type: ", type(scores_array))
print("Dimensions: ", scores_array.ndim)
print("Size: ", scores_array.size)
print("Data type: ", scores_array.dtype)

print("Average: ", round(scores_array.mean(), 2))
print("Maximum: ", scores_array.max())
print("Minimum: ", scores_array.min())
print("Total: ", scores_array.sum())

# Boolean arrays
passed_mask = scores_array >= 5
failed_mask = scores_array <5

print("\nPassed mask: ", passed_mask)
print("Failed mask:", failed_mask)

# Boolean indexing
passed_scores = scores_array[passed_mask]
failed_scores = scores_array[failed_mask]

passed_count = passed_mask.sum()
failed_count = failed_mask.sum()
pass_rate = passed_count / scores_array.size * 100

print("\nPassed students: ", passed_count)
print("Failed students: ", failed_count)
print("Pass rate: ", round(pass_rate,2), "%")
print("Passed scores:", passed_scores)
print("Failed scores:", failed_scores)

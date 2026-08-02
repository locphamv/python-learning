import numpy as np

rng = np.random.default_rng(42)

scores = rng.integers(0, 11, size=20)

print(scores)

print("\nNumber of scores:", scores.size)
print("Average score:", round(scores.mean(), 2))
print("Highest score:", scores.max())
print("Lowest score:", scores.min())

passed_scores = scores[scores >= 5]
failed_scores = scores[scores < 5]
print("\nPassed scores:", passed_scores)
print("Failed scores:", failed_scores)

print("Passed count:", passed_scores.size)
print("Failed count:", failed_scores.size)

passed_rate = passed_scores.size / scores.size * 100
print("Passed rate:", round(passed_rate, 2), "%")

# merge
shuffled_scores = scores.copy()
rng.shuffle(shuffled_scores)

print("\nOriginal scores:")
print(scores)

print("Shuffled scores:")
print(shuffled_scores)

# train and test
test_ratio = 0.2
test_size = int(shuffled_scores.size * test_ratio)

train_scores = shuffled_scores[:-test_size]
test_scores = shuffled_scores[-test_size:]

print("\nTrain scores:", train_scores)
print("Test scores:", test_scores)

print("Train size:", train_scores.size)
print("Test size:", test_scores.size)

print("\nOriginal scores after processing:")
print(scores)

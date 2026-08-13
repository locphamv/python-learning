import numpy as np

scores = np.array([
    4.0,
    5.0,
    6.0,
    6.5,
    7.0,
    7.5,
    8.0,
    8.0,
    9.0,
    10.0,
])

count = scores.size
mean_score = scores.mean()
median_score = np.median(scores)
minimum = scores.min()
maximum = scores.max()
score_range = maximum - minimum
variance = np.var(scores)
standard_deviation = np.std(scores)
q1 = np.percentile(scores, 25)
q2 = np.percentile(scores, 50)
q3 = np.percentile(scores, 75)

print("Count:", count)
print("Mean:", mean_score)
print("Median:", median_score)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Score range:", score_range)
print("Variance:", variance)
print("Standard deviation:", standard_deviation)
print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)

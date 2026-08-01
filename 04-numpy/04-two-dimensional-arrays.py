import numpy as np

scores = np.array([
    [8.0, 7.5, 9.0],
    [6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5],
    [4.0, 5.0, 4.5],
])

print("Score matrix:")
print(scores)

#1. general info
print("\nDimenisons:", scores.ndim)
print("Shape:", scores.shape)
print("Total elements:", scores.size)
print("Data type:", scores.dtype)

#2.  overall average
overall_average = scores.mean()
print("\nOverall average:", round(overall_average,2))

#3. student average
student_averages = scores.mean(axis = 1)
print("Average of each student:", student_averages)

#4. subject average
subject_averages = scores.mean(axis = 0)
print("Average of each subject:", subject_averages)

#5 max score of each student
student_max_scores = scores.max(axis = 1)
print("Highest score of each student:", student_max_scores)

#6 min score
student_min_scores = scores.min(axis = 1)
print("Lowest score of each student:", student_min_scores)

#7 index of max student
best_student_index = student_averages.argmax()
best_student_average = student_averages[best_student_index]

print("\nBest student scores:", best_student_index)
print("Best student average:", best_student_average)

#8. take all best_student_scores
best_student_scores = scores[best_student_index]
print("Best student scores:", best_student_scores)

#9. best_subject_index
best_subject_index = subject_averages.argmax()
best_subject_average = subject_averages[best_subject_index]

print("\nBest subject index:", best_subject_index)
print("Best subject average:", best_subject_average)


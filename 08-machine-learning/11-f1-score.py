import numpy as np
from sklearn.metrics import (
    f1_score,
    precision_score,
    recall_score,
)


y_true = np.array([
    1, 1, 1, 1, 1,
    0, 0, 0, 0, 0,
])


y_pred = np.array([
    1, 1, 1, 0, 0,
    1, 0, 0, 0, 0,
])

precision = precision_score(
    y_true,
    y_pred,
)

recall = recall_score(
    y_true,
    y_pred,
)

print("Precision:", precision)
print("Recall:", recall)


f1 = f1_score(
    y_true,
    y_pred,
)

print("F1 score:", f1)


y_true_2 = np.array([
    1, 1, 1, 1,
    0, 0, 0, 0,
])

y_pred_2 = np.array([
    1, 0, 0, 0,
    0, 0, 0, 0,
])

precision_2 = precision_score(
    y_true_2,
    y_pred_2,
)

recall_2 = recall_score(
    y_true_2,
    y_pred_2,
)

f1_2 = f1_score(
    y_true_2,
    y_pred_2,
)


print("Precision 2:", precision_2)
print("Recall 2:", recall_2)
print("F1 2:", f1_2)

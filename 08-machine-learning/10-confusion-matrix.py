import numpy as np
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
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


matrix = confusion_matrix(
    y_true,
    y_pred,
)

print(matrix)


tn, fp, fn, tp = matrix.ravel()


print("TN:", tn)
print("FP:", fp)
print("FN:", fn)
print("TP:", tp)


accuracy = accuracy_score(
    y_true,
    y_pred,
)

print("Accuracy:", accuracy)


precision = precision_score(
    y_true,
    y_pred,
)

print("Precision:", precision)


recall = recall_score(
    y_true,
    y_pred,
)

print("Recall:", recall)

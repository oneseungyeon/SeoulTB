from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, recall_score, average_precision_score
import numpy as np
import cv2

def compute_iou(y_pred, y_true):
    # ytrue, ypred is a flatten vector
    y_pred = y_pred.flatten()
    y_true = y_true.flatten()
    current = confusion_matrix(y_true, y_pred, labels=[0, 1])
    # compute mean iou
    intersection = np.diag(current)
    ground_truth_set = current.sum(axis=1)
    predicted_set = current.sum(axis=0)
    union = ground_truth_set + predicted_set - intersection
    IoU = intersection / union.astype(np.float32)

    return np.mean(IoU)

def compute_accuracy(y_pred, y_true):
    # ytrue, ypred is a flatten vector
    y_pred = y_pred.flatten()
    y_true = y_true.flatten()
    accuracy = accuracy_score(y_true, y_pred)

    return accuracy

def compute_precision(y_pred, y_true):
    # ytrue, ypred is a flatten vector
    y_pred = y_pred.flatten()
    y_true = y_true.flatten()
    precision = average_precision_score(y_true, y_pred)

    return precision

def compute_recall(y_pred, y_true):
    # ytrue, ypred is a flatten vector
    y_pred = y_pred.flatten()
    y_true = y_true.flatten()
    recall = recall_score(y_true, y_pred, average= None)

    return recall


if __name__ == "__main__" :
    a = cv2.imread("", cv2.IMREAD_COLOR)
    print(a)
    b = cv2.imread("")
    print(b)

    print(compute_iou(a, b))

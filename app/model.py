import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_excel("app/Pumpkin_Seeds_Dataset.xlsx", sheet_name="Pumpkin_Seeds_Dataset")

X = df.drop(columns=["Class"]).values
y = df["Class"].values
unique_classes = np.unique(y)
class_to_int = {name: idx for idx, name in enumerate(unique_classes)}
int_to_class = {idx: name for name, idx in class_to_int.items()}
y_encoded = np.array([class_to_int[label] for label in y])

def standardize(X):
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std

X_scaled = standardize(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.3, random_state=41)

def knn_hard(X_train, y_train, X_test, k=5):
    predictions = []
    for x in X_test:
        distances = np.linalg.norm(X_train - x, axis=1)
        indices = np.argsort(distances)[:k]
        neighbor_labels = y_train[indices]
        values, counts = np.unique(neighbor_labels, return_counts=True)
        predicted_label = values[np.argmax(counts)]
        predictions.append(predicted_label)
    return np.array(predictions)

def knn_soft(X_train, y_train, X_test, k=5):
    predictions = []
    for x in X_test:
        distances = np.linalg.norm(X_train - x, axis=1)
        indices = np.argsort(distances)[:k]
        neighbor_labels = y_train[indices]
        neighbor_distances = distances[indices]

        with np.errstate(divide='ignore'):
            weights = 1 / neighbor_distances
            weights[~np.isfinite(weights)] = 1e10

        vote_weights = {}
        for label, weight in zip(neighbor_labels, weights):
            vote_weights[label] = vote_weights.get(label, 0) + weight

        predicted_label = max(vote_weights.items(), key=lambda x: x[1])[0]
        predictions.append(predicted_label)
    return np.array(predictions)

def predict_knn(sample: list, method: str = "soft", k: int = 3):
    sample = np.array(sample).reshape(1, -1)
    sample = standardize(np.vstack([X, sample]))[-1].reshape(1, -1)

    if method == "hard":
        pred = knn_hard(X_train, y_train, sample, k=k)
    else:
        pred = knn_soft(X_train, y_train, sample, k=k)

    return int_to_class[pred[0]]

#dopisac testy
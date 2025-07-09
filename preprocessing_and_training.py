import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv('data/NF-ToN-IoT.csv')
df['protocol'] = df['protocol'].astype('category').cat.codes
df['Label'] = LabelEncoder().fit_transform(df['Label'])

X = df.drop('Label', axis=1)
y = df['Label']

# Scale and split
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Train models
knn = KNeighborsClassifier(n_neighbors=3)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
knn.fit(X_train, y_train)
rf.fit(X_train, y_train)

# Predict
knn_preds = knn.predict(X_test)
rf_preds = rf.predict(X_test)

# Save models
os.makedirs("models", exist_ok=True)
joblib.dump(knn, "models/knn_model.pkl")
joblib.dump(rf, "models/rf_model.pkl")

# Save confusion matrix plot
os.makedirs("outputs", exist_ok=True)
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, rf_preds), annot=True, cmap='Blues')
plt.title('Random Forest Confusion Matrix')
plt.savefig("outputs/rf_confusion_matrix.png")
plt.close()

# Save classification report
report_text = (
    "KNN Classification Report:\n" +
    classification_report(y_test, knn_preds) +
    "\nRandom Forest Classification Report:\n" +
    classification_report(y_test, rf_preds)
)
with open("outputs/classification_report.txt", "w") as f:
    f.write(report_text)


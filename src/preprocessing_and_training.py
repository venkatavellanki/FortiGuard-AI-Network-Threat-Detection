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

# ✅ Load Dataset
df = pd.read_csv('data/NF-ToN-IoT.csv')
df.dropna(inplace=True)

# 🔃 Encode categorical features
df['protocol'] = df['protocol'].astype('category').cat.codes
df['Label'] = LabelEncoder().fit_transform(df['Label'])

X = df.drop('Label', axis=1)
y = df['Label']

# 📊 Scale Features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 🔀 Split Data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 🧠 Train Models
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# ✅ Predict
knn_preds = knn.predict(X_test)
rf_preds = rf.predict(X_test)

# 📈 Metrics
print("KNN Accuracy:", accuracy_score(y_test, knn_preds))
print("RF Accuracy:", accuracy_score(y_test, rf_preds))

# 📁 Save models
os.makedirs('models', exist_ok=True)
joblib.dump(knn, 'models/knn_model.pkl')
joblib.dump(rf, 'models/rf_model.pkl')

# 📊 Save Confusion Matrix Plot
os.makedirs('outputs', exist_ok=True)
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, rf_preds), annot=True, cmap='Blues')
plt.title('Random Forest Confusion Matrix')
plt.savefig('outputs/rf_confusion_matrix.png')

# 📝 Save Classification Report
with open('outputs/classification_report.txt', 'w') as f:
    f.write("KNN Report:\n")
    f.write(classification_report(y_test, knn_preds))
    f.write("\nRandom Forest Report:\n")
    f.write(classification_report(y_test, rf_preds))

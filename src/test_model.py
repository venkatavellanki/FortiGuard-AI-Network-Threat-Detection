import joblib

rf = joblib.load("models/rf_model.pkl")

# Test on a dummy sample (scaled features)
sample = [[0.0, 0.5, -0.2, 1.0, 0.3]]
prediction = rf.predict(sample)
print("Prediction:", prediction)



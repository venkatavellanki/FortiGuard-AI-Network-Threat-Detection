# 🚨 FortiGuard - AI-Based Cyber Threat Detection System

A machine learning-powered system designed for the real-time detection and counteraction of cyber threats including DDoS, DoS, MITM, and benign traffic. Developed as part of an academic minor project at SRM Institute of Science and Technology.

---

## 📌 Overview

This project leverages supervised learning algorithms like **XGBoost** and **KNN** to analyze network traffic, identify malicious patterns, and automate mitigation strategies. It integrates a multi-layered approach combining anomaly and signature-based techniques with real-time detection and response.

---

## 🛠 Features

- 🔍 Detection of **DDoS**, **DoS**, **MITM**, and **Benign** traffic
- ⚙️ Real-time data processing and classification
- 📊 Confusion matrix and correlation heatmaps
- 📦 Model training using XGBoost and KNN
- 🚨 Autonomous mitigation with alerting and prevention logic
- 📈 High accuracy and performance-tuned classifiers

---

## 📁 Folder Structure

FortiGuard-AI-Network-Threat-Detection/
├── docs/ # Architecture, reports, review PPTs
├── src/ # Python and notebook code
├── models/ # Trained model files (.pkl)
├── data/ # Dataset (if shared)
├── outputs/ # Graphs, classification reports
├── README.md
├── .gitignore
├── requirements.txt


---

## 📦 Installation

Make sure Python 3.8+ is installed.

```bash
pip install -r requirements.txt
```

## 🚀 Run the Notebook

jupyter notebook src/preprocessing_and_training.ipynb

## 📊 Model Performance

- ✅ Accuracy: ~94.88%

- 🧠 Classifiers: XGBoost, KNN

- 📌 Categories Detected: ddos, dos, mitm, benign

## 📚 Documents & Reports

All project documentation is available inside the /docs folder, including:

- Architecture Document

- Functional Document

- Final Report

- Review PPTs (1 to 3)

- Sprint Retrospective

- Functional Test Cases

## 👨‍💻 Developer Info

V. Venkat Aditya
SRM Institute of Science and Technology
Reg No: RA2111003011799

## ⚠️ Disclaimer

This repository is a part of academic coursework and is intended solely for educational and demonstrative purposes.
Reproduction, redistribution, or commercial use of this work is strictly prohibited without explicit written permission from the author.
All rights reserved © 2024 **Venkat Aditya Vellanki**.
